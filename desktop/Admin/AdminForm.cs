using System.Net.Http.Json;
using System.Text.Json.Serialization;
using PiSync.Core.Model;
using PiSync.Core.Network;
using PiSync.Core.Utils;

namespace PiSync.Admin
{
    public partial class AdminForm : Form
    {
        private AdminUpdateMessage admin;
        private string oldPassword;
        public AdminForm()
        {
            InitializeComponent();
        }

        private async void AdminForm_Load(object sender, EventArgs e)
        {
            await FetchAdminDetailsAsync();
        }

        private async Task FetchAdminDetailsAsync()
        {
            try
            {
                var response = await ApiService.httpClient.GetFromJsonAsync<AdminUpdateResponse>($"user/username/{SessionManager.Username}/");
                if (response?.success == true && response.user != null)
                {
                    this.admin = response.user;

                    tbFirstName.Text = admin.first_name;
                    tbLastName.Text = admin.last_name;
                    tbUsername.Text = admin.username;
                    tbPasswordHint.Text = admin.hint_password;
                    tbEmail.Text = admin.email;
                }
                else
                {
                    MessageBox.Show("Failed to load admin details.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show($"Error fetching tenant details: {ex.Message}");
            }
        }

        private async void btnUpdate_Click(object sender, EventArgs e)
        {
            try
            {
                var updateAdmin = new AdminUpdateRequest
                {
                    FirstName = string.IsNullOrWhiteSpace(tbFirstName.Text) ? null : tbFirstName.Text.Trim(),
                    LastName = string.IsNullOrWhiteSpace(tbLastName.Text) ? null : tbLastName.Text.Trim(),
                    Username = string.IsNullOrWhiteSpace(tbUsername.Text) ? null : tbUsername.Text.Trim(),
                    HintPassword = string.IsNullOrWhiteSpace(tbPasswordHint.Text) ? null : tbPasswordHint.Text.Trim(),
                    Email = string.IsNullOrWhiteSpace(tbEmail.Text) ? null : tbEmail.Text.Trim(),
                    Password = string.IsNullOrWhiteSpace(tbPassword.Text) ? null : tbPassword.Text.Trim(),
                };
                System.Diagnostics.Debug.WriteLine($"Update tenant: {updateAdmin}");

                var json = System.Text.Json.JsonSerializer.Serialize(updateAdmin);
                System.Diagnostics.Debug.WriteLine($"Payload to send: {json}");

                var content = new StringContent(json, System.Text.Encoding.UTF8, "application/json");

                var request = new HttpRequestMessage(HttpMethod.Put, $"user/update/{admin.id}/")
                {
                    Content = content
                };

                var response = await ApiService.httpClient.SendAsync(request);
                response.EnsureSuccessStatusCode();

                var result = await response.Content.ReadFromJsonAsync<ApiResponse>();

                if (result?.success == true)
                {
                    await FetchAdminDetailsAsync();

                    if (admin != null)
                    {
                        SessionManager.FullName = $"{admin.first_name} {admin.last_name}";
                        SessionManager.Username = admin.username;
                    }

                    MessageBox.Show("Admin details updated successfully.", "Success", MessageBoxButtons.OK, MessageBoxIcon.Information);
                }
                else
                {
                    string errors = result?.message ?? "Unknown error";
                    MessageBox.Show($"Failed to update admin details: {errors}", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                }
            }
            catch (HttpRequestException httpEx)
            {
                System.Diagnostics.Debug.WriteLine($"HTTP error updating admin: {httpEx.Message}");
                MessageBox.Show($"HTTP error updating admin: {httpEx.Message}", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
            catch (Exception ex)
            {
                System.Diagnostics.Debug.WriteLine($"Error updating admin: {ex.Message}");
                MessageBox.Show($"Error updating admin: {ex.Message}", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }

        }
    }

    internal class ApiResponse
    {
        public bool success { get; set; }
        public string message { get; set; }
    }

    internal class AdminUpdateRequest
    {
        [JsonPropertyName("first_name")]
        [JsonIgnore(Condition = JsonIgnoreCondition.WhenWritingNull)]
        public string? FirstName { get; set; }

        [JsonPropertyName("last_name")]
        [JsonIgnore(Condition = JsonIgnoreCondition.WhenWritingNull)]
        public string? LastName { get; set; }

        [JsonPropertyName("username")]
        [JsonIgnore(Condition = JsonIgnoreCondition.WhenWritingNull)]
        public string? Username { get; set; }

        [JsonPropertyName("hint_password")]
        [JsonIgnore(Condition = JsonIgnoreCondition.WhenWritingNull)]
        public string? HintPassword { get; set; }

        [JsonPropertyName("email")]
        [JsonIgnore(Condition = JsonIgnoreCondition.WhenWritingNull)]
        public string? Email { get; set; }

        [JsonPropertyName("password")]
        [JsonIgnore(Condition = JsonIgnoreCondition.WhenWritingNull)]
        public string? Password { get; set; }
    }
}
