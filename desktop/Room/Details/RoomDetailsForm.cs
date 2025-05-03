using System.Net.Http.Json;
using PiSync.Core.Model;
using PiSync.Core.Network;

namespace PiSync.Room.Details
{
    public partial class RoomDetailsForm : Form
    {
        private RoomModel room = new RoomModel();
        private readonly HttpClient httpClient = new HttpClient { BaseAddress = new Uri(ApiService.BASE_URL) };

        public RoomDetailsForm(int roomId, string roomName)
        {
            InitializeComponent();

            room.id = roomId;
            room.name = roomName;

            LoadRoomDetailsAsync();
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
