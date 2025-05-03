using System.Text;
using System.Text.Json;
using PiSync.Core.Network;

namespace PiSync.Room.NewRoom
{
    public partial class NewRoomForm : Form
    {
        private readonly HttpClient httpClient = new HttpClient();
        public NewRoomForm()
        {
            InitializeComponent();
        }

        private void btnCancel_Click(object sender, EventArgs e)
        {
            Hide();
        }

        private async void btnSave_Click(object sender, EventArgs e)
        {
            var roomName = tbRoomName.Text.Trim();

            if (string.IsNullOrEmpty(roomName))
            {
                MessageBox.Show("Please enter a room name");
                return;
            }
            Console.WriteLine($"Room name: {roomName}");

            bool isSaved = await SaveRoomToDatabase(roomName);
            if (isSaved)
            {
                Hide();
            }
        }

        private async Task<bool> SaveRoomToDatabase(string roomName)
        {
            try
            {
                var roomData = new
                {
                    name = roomName
                };
                string json = JsonSerializer.Serialize(roomData);
                var content = new StringContent(json, Encoding.UTF8, "application/json");

                var response = await httpClient.PostAsync($"{ApiService.BASE_URL}door/new/", content);

                if (response.IsSuccessStatusCode)
                {
                    string result = await response.Content.ReadAsStringAsync();
                    Console.WriteLine($"Server response: {result}");
                    MessageBox.Show("Room saved successfully");
                    return true;
                }
                else
                {
                    string error = await response.Content.ReadAsStringAsync();
                    Console.WriteLine($"Save failed: {error}");
                    MessageBox.Show($"Error: {response.StatusCode}\n{error}");
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Error: {ex.Message}");
                MessageBox.Show($"Exception: {ex.Message}");
            }
            return false;
        }
    }
}
