﻿using System.Net.Http.Json;
using System.Text.Json.Serialization;
using PiSync.Core.Helpers;
using PiSync.Core.Model;
using PiSync.Core.Network;

namespace PiSync.Tenant.Update
{
    public partial class TenantUpdateForm : Form
    {
        private int tenantId;
        private TenantUpdateMessage tenant;
        private string? initial_fingerprint = null;

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

                var selectedTemplate = tbFingerprint.Text.Trim();  // This will be null if nothing is selected  
                if (selectedTemplate == "Select fingerprint")
                {
                    selectedTemplate = null;
                }
                System.Diagnostics.Debug.WriteLine($"tb fingerprint text: `{tbFingerprint.Text}`");
                System.Diagnostics.Debug.WriteLine($"Selected template: `{selectedTemplate}`");

                var updateTenant = new TenantUpdateRequest
                {
                    FirstName = string.IsNullOrWhiteSpace(tbFirstName.Text) ? null : tbFirstName.Text.Trim(),
                    LastName = string.IsNullOrWhiteSpace(tbLastName.Text) ? null : tbLastName.Text.Trim(),
                    Username = string.IsNullOrWhiteSpace(tbUsername.Text) ? null : tbUsername.Text.Trim(),
                    HintPassword = string.IsNullOrWhiteSpace(tbPasswordHint.Text) ? null : tbPasswordHint.Text.Trim(),
                    Gender = string.IsNullOrWhiteSpace(tbGender.Text) ? null : tbGender.Text.Trim(),
                    Email = string.IsNullOrWhiteSpace(tbEmail.Text) ? null : tbEmail.Text.Trim(),
                    FingerprintTemplate = selectedTemplate,
                    Password = string.IsNullOrWhiteSpace(tbPassword.Text) ? null : tbPassword.Text.Trim(),
                    RegisteredDoors = doorIds
                };
                System.Diagnostics.Debug.WriteLine($"Update tenant: {updateTenant}");

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
                    // lets unassign it now;
                    // endpoint is: /fingerprint/unassign/initial_fingerprint/
                    // lets assign the new fingerprint if it is not null
                    // endpoint is: /fingerprint/assign/selectedTemplate/
                    if (initial_fingerprint != selectedTemplate)
                    {
                        try
                        {
                            async Task<HttpResponseMessage> PatchAsync(string url)
                            {
                                var method = new HttpMethod("PATCH");
                                var request = new HttpRequestMessage(method, url)
                                {
                                    Content = new StringContent(string.Empty) // Empty content for PATCH
                                };
                                return await ApiService.httpClient.SendAsync(request);
                            }

                            // Unassign old fingerprint if it exists and is not default placeholder
                            if (!string.IsNullOrWhiteSpace(initial_fingerprint) && initial_fingerprint != "Select fingerprint")
                            {
                                var unassignResponse = await PatchAsync($"fingerprint/unassign/{initial_fingerprint}/");
                                if (!unassignResponse.IsSuccessStatusCode)
                                {
                                    var error = await unassignResponse.Content.ReadAsStringAsync();
                                    System.Diagnostics.Debug.WriteLine($"Failed to unassign fingerprint {initial_fingerprint}: {error}");
                                }
                            }

                            // If selectedTemplate is not null/empty/placeholder, assign it
                            if (!string.IsNullOrWhiteSpace(selectedTemplate) && selectedTemplate != "Select fingerprint")
                            {
                                var assignResponse = await PatchAsync($"fingerprint/assign/{selectedTemplate}/");
                                if (!assignResponse.IsSuccessStatusCode)
                                {
                                    var error = await assignResponse.Content.ReadAsStringAsync();
                                    System.Diagnostics.Debug.WriteLine($"Failed to assign fingerprint {selectedTemplate}: {error}");
                                }
                            }
                            else
                            {
                                // selectedTemplate is null/empty, so only unassignment is done (already done above)
                                System.Diagnostics.Debug.WriteLine("Selected template is null or empty, only unassign performed.");
                            }
                        }
                        catch (Exception ex)
                        {
                            System.Diagnostics.Debug.WriteLine($"Error during fingerprint assign/unassign: {ex.Message}");
                        }
                    }
                    else
                    {
                        // initial_fingerprint == selectedTemplate, no change needed
                        System.Diagnostics.Debug.WriteLine("Fingerprint unchanged, no assign/unassign performed.");
                    }

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

            var fingerprints = await FetchFingerprintTemplatesAsync();

            fingerprints.Insert(0, new FingerprintTemplate
            {
                Name = "Select fingerprint",
                Template = null
            });

            // If tenant has a fingerprint assigned, fetch and insert it manually
            if (!string.IsNullOrWhiteSpace(tenant?.fingerprint_template) && tenant.fingerprint_template != "No fingerprint template")
            {
                var currentFingerprint = await FetchFingerprintDetailAsync(tenant.fingerprint_template);

                if (currentFingerprint != null)
                {
                    // Avoid duplicate entries (e.g., if template is mistakenly in the unassigned list)
                    if (!fingerprints.Any(f => f.Name == currentFingerprint.Name))
                    {
                        fingerprints.Insert(1, currentFingerprint);
                    }
                }
            }

            tbFingerprint.DataSource = fingerprints;
            tbFingerprint.DisplayMember = "Name";
            tbFingerprint.ValueMember = "Name";
            tbFingerprint.SelectedIndex = 0;

            // Select current assigned fingerprint if present
            if (!string.IsNullOrWhiteSpace(tenant?.fingerprint_template) &&
                tenant.fingerprint_template != "No fingerprint template")
            {
                var index = fingerprints.FindIndex(f => f.Name == tenant.fingerprint_template);
                tbFingerprint.SelectedIndex = index >= 0 ? index : 0;
            }
            else
            {
                tbFingerprint.SelectedIndex = 0;
            }
            initial_fingerprint = tbFingerprint.Text.Trim();
            System.Diagnostics.Debug.WriteLine($"Initial fingerprint: `{initial_fingerprint}`");
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
                    tbEmail.Text = tenant.email;
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

        private async Task<List<FingerprintTemplate>> FetchFingerprintTemplatesAsync()
        {
            try
            {
                var response = await ApiService.httpClient.GetAsync("fingerprint/");
                if (response.IsSuccessStatusCode)
                {
                    var templates = await response.Content.ReadFromJsonAsync<List<FingerprintTemplate>>();
                    return templates ?? new List<FingerprintTemplate>();
                }
                else
                {
                    string error = await response.Content.ReadAsStringAsync();
                    System.Diagnostics.Debug.WriteLine($"Failed to fetch fingerprints: {error}");
                }
            }
            catch (Exception ex)
            {
                System.Diagnostics.Debug.WriteLine($"Exception fetching fingerprints: {ex.Message}");
            }
            return new List<FingerprintTemplate>();
        }

        private async Task<FingerprintTemplate?> FetchFingerprintDetailAsync(string fingerprintName)
        {
            if (string.IsNullOrWhiteSpace(fingerprintName) || fingerprintName == "Select fingerprint")
                return null;

            try
            {
                var response = await ApiService.httpClient.GetAsync($"fingerprint/details/{fingerprintName}/");
                if (response.IsSuccessStatusCode)
                {
                    var detail = await response.Content.ReadFromJsonAsync<FingerprintTemplate>();
                    return detail;
                }
                else
                {
                    string error = await response.Content.ReadAsStringAsync();
                    System.Diagnostics.Debug.WriteLine($"Failed to fetch fingerprint details: {error}");
                }
            }
            catch (Exception ex)
            {
                System.Diagnostics.Debug.WriteLine($"Exception fetching fingerprint details: {ex.Message}");
            }
            return null;
        }

        private async void tbFingerprint_SelectedIndexChanged(object sender, EventArgs e)
        {
            if (tbFingerprint.SelectedItem is FingerprintTemplate selectedFingerprint)
            {
                var detail = await FetchFingerprintDetailAsync(selectedFingerprint.Name);
                if (detail != null)
                {
                    tbFingerprint.Text = detail.Name ?? "";
                    System.Diagnostics.Debug.WriteLine($"Loaded fingerprint template for {detail.Name}");
                }
                else
                {
                    tbFingerprint.Text = "";
                }
            }
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

        [JsonPropertyName("email")]
        [JsonIgnore(Condition = JsonIgnoreCondition.WhenWritingNull)]
        public string? Email { get; set; }

        [JsonPropertyName("fingerprint_template")]
        public string? FingerprintTemplate { get; set; }

        [JsonPropertyName("password")]
        [JsonIgnore(Condition = JsonIgnoreCondition.WhenWritingNull)]
        public string? Password { get; set; }

        [JsonPropertyName("registered_doors")]
        public List<int> RegisteredDoors { get; set; } = new();
    }


}
