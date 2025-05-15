using System.Net.Http.Json;
using PiSync.Core.Helpers;
using PiSync.Core.Model;
using PiSync.Core.Network;
using System.Text.Json.Serialization;

namespace PiSync.Tenant.Update
{
    public partial class TenantUpdateForm : Form
    {
        private int tenantId;
        private TenantUpdateMessage tenant;

        public TenantUpdateForm(int tenantId)
        {
            InitializeComponent();
            this.tenantId = tenantId;
        }

        private async void btnUpdate_Click(object sender, EventArgs e)
        {
            try
            {
                var registeredDoorText = tbRegisteredDoors.Text.Trim();
                List<int> doorIds;

                if (registeredDoorText.Equals("No rooms", StringComparison.OrdinalIgnoreCase) ||
                    string.IsNullOrEmpty(registeredDoorText))
                {
                    doorIds = new List<int>();
                }
                else
                {
                    doorIds = await RoomHelper.ParseRoomNamesToIdsAsync(registeredDoorText);
                    if (doorIds == null)
                    {
                        MessageBox.Show("One or more rooms could not be resolved to IDs.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                        return;
                    }
                }

                var updateTenant = new TenantUpdateRequest
                {
                    FirstName = string.IsNullOrWhiteSpace(tbFirstName.Text) ? null : tbFirstName.Text.Trim(),
                    LastName = string.IsNullOrWhiteSpace(tbLastName.Text) ? null : tbLastName.Text.Trim(),
                    Username = string.IsNullOrWhiteSpace(tbUsername.Text) ? null : tbUsername.Text.Trim(),
                    HintPassword = string.IsNullOrWhiteSpace(tbPasswordHint.Text) ? null : tbPasswordHint.Text.Trim(),
                    Gender = string.IsNullOrWhiteSpace(tbGender.Text) ? null : tbGender.Text.Trim(),
                    FingerprintTemplate = string.IsNullOrWhiteSpace(tbFingerprint.Text) ? null : tbFingerprint.Text.Trim(),
                    Password = string.IsNullOrWhiteSpace(tbPassword.Text) ? null : tbPassword.Text.Trim(),
                    RegisteredDoors = doorIds
                };

                var json = System.Text.Json.JsonSerializer.Serialize(updateTenant);
                System.Diagnostics.Debug.WriteLine($"Payload to send: {json}");

                var content = new StringContent(json, System.Text.Encoding.UTF8, "application/json");

                var request = new HttpRequestMessage(HttpMethod.Put, $"user/update/{tenantId}/")
                {
                    Content = content
                };

                var response = await ApiService.httpClient.SendAsync(request);
                response.EnsureSuccessStatusCode();

                var result = await response.Content.ReadFromJsonAsync<ApiResponse>();

                if (result?.success == true)
                {
                    MessageBox.Show("Tenant updated successfully.", "Success", MessageBoxButtons.OK, MessageBoxIcon.Information);
                }
                else
                {
                    string errors = result?.message ?? "Unknown error";
                    MessageBox.Show($"Failed to update tenant: {errors}", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                }
            }
            catch (HttpRequestException httpEx)
            {
                System.Diagnostics.Debug.WriteLine($"HTTP error updating tenant: {httpEx.Message}");
                MessageBox.Show($"HTTP error updating tenant: {httpEx.Message}", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
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
                var response = await ApiService.httpClient.GetFromJsonAsync<TenantUpdateResponse>($"user/{tenantId}/");
                if (response?.success == true && response.user != null)
                {
                    this.tenant = response.user;

                    tbFirstName.Text = tenant.first_name;
                    tbLastName.Text = tenant.last_name;
                    tbUsername.Text = tenant.username;
                    tbPasswordHint.Text = tenant.hint_password;
                    tbGender.Text = tenant.gender;
                    tbFingerprint.Text = string.IsNullOrEmpty(tenant.fingerprint_template) ? "No fingerprint template" : tenant.fingerprint_template;

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
                tbRegisteredDoors.Text = "No rooms";
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

    internal class ApiResponse
    {
        public bool success { get; set; }
        public string message { get; set; }
    }

    internal class TenantUpdateRequest
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

        [JsonPropertyName("gender")]
        [JsonIgnore(Condition = JsonIgnoreCondition.WhenWritingNull)]
        public string? Gender { get; set; }

        [JsonPropertyName("fingerprint_template")]
        [JsonIgnore(Condition = JsonIgnoreCondition.WhenWritingNull)]
        public string? FingerprintTemplate { get; set; }

        [JsonPropertyName("password")]
        [JsonIgnore(Condition = JsonIgnoreCondition.WhenWritingNull)]
        public string? Password { get; set; }

        [JsonPropertyName("registered_doors")]
        public List<int> RegisteredDoors { get; set; } = new();
    }


}
