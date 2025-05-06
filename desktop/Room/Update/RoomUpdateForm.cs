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
            tbDoorStatus.Text = room.isOpen ? "Open" : "Closed";
            tbRoomStatus.Text = room.isActive ? "Active" : "Inactive";
        }

        private void btnUpdate_Click(object sender, EventArgs e)
        {
            string roomName = tbRoomName.Text.Trim();
            string doorStatus = tbDoorStatus.Text.Trim();
            string roomStatus = tbRoomStatus.Text.Trim();

            System.Diagnostics.Debug.WriteLine($"Room name: `{roomName}`, doorStatus: `{doorStatus}`, roomStatus: `{roomStatus}`"); ;
        }
    }
}
