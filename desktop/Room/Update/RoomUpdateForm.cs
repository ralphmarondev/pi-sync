using System.Net.Http.Json;
using PiSync.Core.Model;
using PiSync.Core.Network;

namespace PiSync.Room.Update
{
    public partial class RoomUpdateForm : Form
    {
        private RoomModel room = new RoomModel();

        public RoomUpdateForm(int roomId, string roomName)
        {
            InitializeComponent();

            room.id = roomId;
            room.name = roomName;
        }

        private void RoomUpdateForm_Load(object sender, EventArgs e)
        {
            LoadRoomDetailsAsync();
        }


        private async void LoadRoomDetailsAsync()
        {
            try
            {
                var response = await ApiService.httpClient.GetFromJsonAsync<RoomModel>($"door/{room.id}/");
                if (response != null)
                {
                    room = response;
                    PopulateDetails();
                }
                else
                {
                    MessageBox.Show("Room details not found.");
                }

            }
            catch (Exception ex)
            {
                MessageBox.Show($"Failed to load room details: {ex.Message}");
            }
        }

        private void PopulateDetails()
        {
            tbRoomName.Text = room.name;
            tbDoorStatus.Text = room.isOpen ? "OPEN" : "CLOSED";
            tbRoomStatus.Text = room.isActive ? "ACTIVE" : "INACTIVE";
        }

        private async void btnUpdate_Click(object sender, EventArgs e)
        {
            string roomName = tbRoomName.Text.Trim();
            string doorStatus = tbDoorStatus.Text.Trim();
            string roomStatus = tbRoomStatus.Text.Trim();

            bool isOpen = doorStatus.Equals("OPEN", StringComparison.OrdinalIgnoreCase);
            bool isActive = roomStatus.Equals("ACTIVE", StringComparison.OrdinalIgnoreCase);

            System.Diagnostics.Debug.WriteLine($"Room name: `{roomName}`, doorStatus: `{doorStatus}`, roomStatus: `{roomStatus}`, isOpen: `{isOpen}`, isActive: `{isActive}`");

            room.name = roomName;
            room.isOpen = isOpen;
            room.isActive = isActive;

            try
            {
                var json = System.Text.Json.JsonSerializer.Serialize(room);
                var content = new StringContent(json, System.Text.Encoding.UTF8, "application/json");

                var request = new HttpRequestMessage(HttpMethod.Put, $"door/update/{room.id}/")
                {
                    Content = content
                };

                var response = await ApiService.httpClient.SendAsync(request);
                response.EnsureSuccessStatusCode();

                var result = await response.Content.ReadFromJsonAsync<ApiResponse<RoomModel>>();

                if (result?.success == true)
                {
                    MessageBox.Show("Room updated successfully!", "Success", MessageBoxButtons.OK, MessageBoxIcon.Information);
                }
                else
                {
                    string errors = result?.message ?? "Unknown error";
                    MessageBox.Show($"Failed to update room: {errors}", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                }
            }
            catch (Exception ex)
            {
                System.Diagnostics.Debug.WriteLine($"Error updating room: {ex.Message}");
                MessageBox.Show($"Error updating room: {ex.Message}", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }
    }
}
