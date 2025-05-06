using System.Net.Http.Json;
using PiSync.Core.Model;
using PiSync.Core.Network;

namespace PiSync.Tenant.Update
{
    public partial class TenantUpdateForm : Form
    {
        private int tenantId;
        private UserModel tenant;

        public TenantUpdateForm(int tenantId)
        {
            InitializeComponent();
            this.tenantId = tenantId;
        }
        private async void btnUpdate_Click(object sender, EventArgs e)
        {
            // Build a user object from form fields
            UserModel updatedUser = new UserModel
            {
                first_name = tbFirstName.Text.Trim(),
                last_name = tbLastName.Text.Trim(),
                username = tbUsername.Text.Trim(),
                hint_password = tbPasswordHint.Text.Trim(),
                gender = tbGender.Text.Trim(),
                registered_doors = tenant.registered_doors  // Keep current doors
            };

            string password = tbPassword.Text.Trim();

            // Build form data
            var formData = new List<KeyValuePair<string, string>>
            {
                new KeyValuePair<string, string>("first_name", updatedUser.first_name),
                new KeyValuePair<string, string>("last_name", updatedUser.last_name),
                new KeyValuePair<string, string>("username", updatedUser.username),
                new KeyValuePair<string, string>("hint_password", updatedUser.hint_password),
                new KeyValuePair<string, string>("gender", updatedUser.gender),
            };

            // Optional password update
            if (!string.IsNullOrEmpty(password))
            {
                formData.Add(new KeyValuePair<string, string>("password", password));
            }

            // Registered doors
            foreach (var doorId in updatedUser.registered_doors)
            {
                formData.Add(new KeyValuePair<string, string>("registered_doors", doorId.ToString()));
            }

            var content = new FormUrlEncodedContent(formData);

            try
            {
                var response = await ApiService.httpClient.PutAsync($"user/update/{tenantId}/", content);
                response.EnsureSuccessStatusCode();

                // Deserialize with your ApiResponse<UserModel>
                var result = await response.Content.ReadFromJsonAsync<ApiResponse<UserModel>>();

                if (result?.success == true)
                {
                    MessageBox.Show("Tenant updated successfully!", "Success", MessageBoxButtons.OK, MessageBoxIcon.Information);

                    // Optional: update the local tenant object with the latest data from server
                    this.tenant = result.users;
                }
                else
                {
                    string errors = result?.message ?? "Unknown error";
                    MessageBox.Show($"Failed to update tenant: {errors}", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                }
            }
            catch (Exception ex)
            {
                System.Diagnostics.Debug.WriteLine($"Error updating tenant: {ex.Message}");
                MessageBox.Show($"Error updating tenant: {ex.Message}", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }

        private async void TenantUpdateForm_Load(object sender, EventArgs e)
        {
            await FetchTenantDetailsAsync();
        }


        private async Task FetchTenantDetailsAsync()
        {
            try
            {
                var response = await ApiService.httpClient.GetFromJsonAsync<TenantDetailsResponse>($"user/{tenantId}/");
                if (response?.success == true && response.message != null)
                {
                    this.tenant = response.message;

                    tbFirstName.Text = tenant.first_name;
                    tbLastName.Text = tenant.last_name;
                    tbUsername.Text = tenant.username;
                    tbPasswordHint.Text = tenant.hint_password;
                    tbGender.Text = tenant.gender;

                    await LoadRegisteredDoorNameAsync(tenant.registered_doors);
                }
                else
                {
                    MessageBox.Show("Failed to load tenant details.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show($"Error fetching tenant details: {ex.Message}");
            }
        }

        private async Task LoadRegisteredDoorNameAsync(List<int> doorIds)
        {
            if (doorIds == null || doorIds.Count == 0)
            {
                System.Diagnostics.Debug.WriteLine($"No rooms. Door count: {doorIds?.Count}");
                tbRegisteredDoors.Text = "No roooms";
                return;
            }

            List<string> doorNames = new List<string>();

            foreach (var doorId in doorIds)
            {
                try
                {
                    var room = await ApiService.httpClient.GetFromJsonAsync<RoomModel>($"door/{doorId}/");
                    if (room != null)
                    {
                        doorNames.Add(room.name);
                    }
                }
                catch (Exception ex)
                {
                    System.Diagnostics.Debug.WriteLine($"Error fetching door {doorId}: {ex.Message}");
                    doorNames.Add("Unknown door");
                }
            }
            tbRegisteredDoors.Text = doorNames.Count > 0 ? string.Join(", ", doorNames) : "No rooms";
        }
    }
}
