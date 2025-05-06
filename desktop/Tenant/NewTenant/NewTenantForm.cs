using System.Net.Http.Json;
using PiSync.Core.Model;
using PiSync.Core.Network;

namespace PiSync.Tenant.NewTenant
{
    public partial class NewTenantForm : Form
    {
        public NewTenantForm()
        {
            InitializeComponent();
        }

        private void btnCancel_Click(object sender, EventArgs e)
        {
            Hide();
        }

        private async void btnSave_Click(object sender, EventArgs e)
        {
            string firstName = tbFirstName.Text.Trim();
            string lastName = tbLastName.Text.Trim();
            string username = tbUsername.Text.Trim();
            string password = tbPassword.Text.Trim();
            string passwordHint = tbPasswordHint.Text.Trim(); // optional, can be empty.
            string gender = tbGender.Text.Trim();

            string registeredDoorText = tbRegisteredDoors.Text.Trim();
            List<string> registeredDoorList = registeredDoorText
                .Split(new char[] { ',' }, StringSplitOptions.RemoveEmptyEntries)
                .Select(s => s.Trim())
                .ToList();

            System.Diagnostics.Debug.WriteLine($"First name: `{firstName}`, Last name: `{lastName}`, username: `{username}`, password: `{password}`, passwordHint: `{passwordHint}`, gender: `{gender}`");
            System.Diagnostics.Debug.WriteLine($"Registered doors:");
            foreach (var item in registeredDoorList)
            {
                System.Diagnostics.Debug.WriteLine($"`{item}`");
            }

            if (
                string.IsNullOrEmpty(firstName) ||
                string.IsNullOrEmpty(lastName) ||
                string.IsNullOrEmpty(username) ||
                string.IsNullOrEmpty(gender) ||
                string.IsNullOrEmpty(password) ||
                registeredDoorList.Count < 1)
            {
                ShowWarning("Please fill out all required fields.");
                return;
            }

            if (string.IsNullOrEmpty(firstName))
            {
                ShowWarning("First name cannot be empty.");
                return;
            }
            if (string.IsNullOrEmpty(lastName))
            {
                ShowWarning("Last name cannot be empty.");
                return;
            }
            if (string.IsNullOrEmpty(username))
            {
                ShowWarning("Username cannot be empty.");
                return;
            }
            if (string.IsNullOrEmpty(gender))
            {
                ShowWarning("Gender cannot be empty.");
                return;
            }
            if (string.IsNullOrEmpty(password))
            {
                ShowWarning("Password cannot be empty.");
                return;
            }
            if (registeredDoorList.Count < 1)
            {
                ShowWarning("Registered doors cannot be empty.");
                return;
            }

            Console.WriteLine("Saving to database...");

            var doorIds = new List<int>();
            foreach (var doorName in registeredDoorList)
            {
                var doorId = await GetRoomIdByNameAsync(doorName);
                if (doorId.HasValue)
                {
                    doorIds.Add(doorId.Value);
                }
                else
                {
                    MessageBox.Show($"Room `{doorName}` not found.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                    return;
                }
            }
            Console.WriteLine("All doors found. Proceeding to save...");

            bool success = await SaveTenantAsync(firstName, lastName, username, password, passwordHint, gender, doorIds);
            if (success)
            {
                MessageBox.Show("Tenant registered successfully!", "Success", MessageBoxButtons.OK, MessageBoxIcon.Information);
                Hide();
            }
            else
            {
                MessageBox.Show("Failed to register tenant. Please try again.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }

        private static void ShowWarning(string message)
        {
            MessageBox.Show(message, "Error", MessageBoxButtons.OK, MessageBoxIcon.Warning);
        }

        // saving to api lol
        private async Task<bool> SaveTenantAsync(string firstName, string lastName, string username, string password, string passwordHint, string gender, List<int> registeredDoorList)
        {
            var requestBody = new RegisterTenantRequest
            {
                Username = username,
                FirstName = firstName,
                LastName = lastName,
                Password = password,
                HintPassword = passwordHint,
                Gender = gender,
                RegisteredDoors = registeredDoorList
            };

            // 🟠 Debug print: Show the JSON payload before sending
            string jsonPayload = System.Text.Json.JsonSerializer.Serialize(requestBody, new System.Text.Json.JsonSerializerOptions { WriteIndented = true });
            System.Diagnostics.Debug.WriteLine("➡️ Sending JSON payload:\n" + jsonPayload);

            try
            {
                // 🔥 Use HttpRequestMessage to ensure correct Content-Type and view raw JSON
                var request = new HttpRequestMessage(HttpMethod.Post, "register/")
                {
                    Content = JsonContent.Create(requestBody)
                };

                // 🟠 Debug print: show raw content (should look like JSON)
                string rawContent = await request.Content.ReadAsStringAsync();
                System.Diagnostics.Debug.WriteLine("➡️ Raw HTTP Body being sent:\n" + rawContent);

                var response = await ApiService.httpClient.SendAsync(request);

                if (response.IsSuccessStatusCode)
                {
                    return true;
                }
                else
                {
                    string error = await response.Content.ReadAsStringAsync();
                    System.Diagnostics.Debug.WriteLine($"API error: {error}");
                    return false;
                }
            }
            catch (Exception ex)
            {
                System.Diagnostics.Debug.WriteLine($"Exception: {ex.Message}");
                return false;
            }
        }

        private async Task<int?> GetRoomIdByNameAsync(string roomName)
        {
            try
            {
                string url = $"door/name/{roomName}/";
                var response = await ApiService.httpClient.GetAsync(url);

                if (response.IsSuccessStatusCode)
                {
                    var roomResponse = await response.Content.ReadFromJsonAsync<RoomResponse>();

                    if (roomResponse != null && roomResponse.Door != null)
                    {
                        return roomResponse.Door.Id;
                    }
                    else
                    {
                        System.Diagnostics.Debug.WriteLine("Room not found in the response");
                    }
                }
                else
                {
                    string error = await response.Content.ReadAsStringAsync();
                    System.Diagnostics.Debug.WriteLine($"Room lookup failed. {error}");
                }
            }
            catch (Exception ex)
            {
                System.Diagnostics.Debug.WriteLine($"Exception in GetRoomIdByNameAsync: {ex.Message}");
            }
            return null;
        }
    }
}