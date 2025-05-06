using System.Net.Http.Json;
using PiSync.Core.Model;
using PiSync.Core.Network;

namespace PiSync.Tenant.Details
{
    public partial class TenantDetailsForm : Form
    {
        private int tenantId;
        private string tenantName;
        public TenantDetailsForm(int tenantId, string tenantName)
        {
            InitializeComponent();

            this.tenantId = tenantId;
            this.tenantName = tenantName;
        }

        private async void TenantDetailsForm_Load(object sender, EventArgs e)
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
                    TenantDetailsMessage tenant = response.message;

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