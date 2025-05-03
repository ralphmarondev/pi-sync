using System.Net.Http.Json;
using PiSync.Core.Model;
using PiSync.Core.Network;

namespace PiSync.Room.Delete
{
    public partial class RoomDeleteForm : Form
    {
        private RoomModel room = new RoomModel();
        private readonly HttpClient httpClient = new HttpClient { BaseAddress = new Uri(ApiService.BASE_URL) };

        public RoomDeleteForm(int roomId, string roomName)
        {
            InitializeComponent();

            room.id = roomId;
            room.name = roomName;

            LoadRoomDetailsAsync();
        }

        private async void btnDelete_Click(object sender, EventArgs e)
        {
            var confirmResult = MessageBox.Show($"Are you sure you want to delete room `{room.name}`?",
                "Confirm Delete",
                MessageBoxButtons.YesNo,
                MessageBoxIcon.Warning);

            if (confirmResult == DialogResult.Yes)
            {
                try
                {
                    var deleteRoom = new { is_deleted = true };
                    var response = await httpClient.PutAsJsonAsync($"door/delete/{room.id}/", deleteRoom);

                    if (response.IsSuccessStatusCode)
                    {
                        MessageBox.Show("Room deleted successfully.", "Success", MessageBoxButtons.OK, MessageBoxIcon.Information);
                        Close();
                    }
                    else
                    {
                        var errorContent = await response.Content.ReadAsStringAsync();
                        MessageBox.Show($"Failed to delete room. Server says: {errorContent}", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                    }
                }
                catch (Exception ex)
                {
                    System.Diagnostics.Debug.WriteLine($"Error deleting room: {ex.Message}");
                    MessageBox.Show($"Error occured: {ex.Message}", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                }
            }
        }


        private async void LoadRoomDetailsAsync()
        {
            try
            {
                var response = await httpClient.GetFromJsonAsync<RoomModel>($"door/{room.id}/");
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
            lblRoomName.Text = room.name;
            lblDoorStatus.Text = room.isOpen ? "Open" : "Closed";
            lblRoomStatus.Text = room.isActive ? "Active" : "Inactive";
            lblTenantCount.Text = room.tenantCount.ToString();
        }
    }
}
