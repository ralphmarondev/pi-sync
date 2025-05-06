using System.Net.Http.Json;
using PiSync.Core.Model;
using PiSync.Core.Network;

namespace PiSync.Tenant.Update
{
    public partial class TenantUpdateForm : Form
    {
        private int tenantId;
        private TenantDetailsMessage tenant;

        public TenantUpdateForm(int tenantId)
        {
            InitializeComponent();
            this.tenantId = tenantId;
        }

        private async void btnUpdate_Click(object sender, EventArgs e)
        {

            string firstName = tbFirstName.Text.Trim();
            string lastName = tbLastName.Text.Trim();
            string username = tbUsername.Text.Trim();
            string password = tbPassword.Text.Trim();  // Add this textbox in your form if you want to allow password updates
            string passwordHint = tbPasswordHint.Text.Trim();
            string gender = tbGender.Text.Trim();

            // Prepare the updated data payload
            var updatedUser = new
            {
                first_name = firstName,
                last_name = lastName,
                username = username,
                password = string.IsNullOrEmpty(password) ? null : password, // Only send password if not empty
                hint_password = passwordHint,
                gender = gender,
                registered_doors = tenant.registered_doors // Reuse existing registered doors
            };

            try
            {
                var response = await ApiService.httpClient.PutAsJsonAsync($"user/update/{tenantId}/", updatedUser);
                response.EnsureSuccessStatusCode();

                var result = await response.Content.ReadFromJsonAsync<ApiResponse<object>>();

                if (result?.success == true)
                {
                    MessageBox.Show("Tenant updated successfully!", "Success", MessageBoxButtons.OK, MessageBoxIcon.Information);
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
