using System.Net.Http.Json;
using PiSync.Core.Model;
using PiSync.Core.Network;

namespace PiSync.Tenant
{
    public partial class TenantForm : Form
    {
        private List<UserModel> tenants = new List<UserModel>();
        public TenantForm()
        {
            InitializeComponent();
            SetupDataGridView();
            FetchTenantsAsync();
        }

        private void btnNewTenant_Click(object sender, EventArgs e)
        {
            NewTenantForm form = new NewTenantForm();
            form.ShowDialog(this);
        }


        // Setup DataGridView to display tenant data
        private void SetupDataGridView()
        {
            dataGridViewTenant.Columns.Clear();
            dataGridViewTenant.SelectionMode = DataGridViewSelectionMode.FullRowSelect;

            dataGridViewTenant.Columns.Add("id", "ID");
            dataGridViewTenant.Columns["id"].Visible = false;

            dataGridViewTenant.Columns.Add("fullName", "Full Name");
            dataGridViewTenant.Columns.Add("email", "Email");
            dataGridViewTenant.Columns.Add("rooms", "Rooms");

            dataGridViewTenant.AutoSizeColumnsMode = DataGridViewAutoSizeColumnsMode.Fill;
            dataGridViewTenant.ReadOnly = true;
            dataGridViewTenant.AllowUserToAddRows = false;
            dataGridViewTenant.AllowUserToDeleteRows = false;
            dataGridViewTenant.RowTemplate.Height = 60;
            dataGridViewTenant.DefaultCellStyle.WrapMode = DataGridViewTriState.True;

            dataGridViewTenant.DefaultCellStyle.Font = new Font("Courier New", 14);
            dataGridViewTenant.ColumnHeadersDefaultCellStyle.Font = new Font("Courier New", 14, FontStyle.Bold);
            dataGridViewTenant.ColumnHeadersDefaultCellStyle.ForeColor = Color.Purple;
            dataGridViewTenant.EnableHeadersVisualStyles = false;

            SetDataGridViewPadding();
        }

        // Fetch tenants from the API
        private async void FetchTenantsAsync()
        {
            try
            {
                var response = await ApiService.httpClient.GetFromJsonAsync<ApiResponse<List<UserModel>>>("users/");
                if (response?.success == true)
                {
                    tenants = response.users;
                    PopulateTenants();
                }
                else
                {
                    ShowEmptyMessage();
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show($"Failed to fetch tenants: {ex.Message}");
            }
        }

        // Populate the DataGridView with tenants' information
        private async Task PopulateTenants()
        {
            lblEmpty.Visible = tenants.Count == 0;
            dataGridViewTenant.Rows.Clear();

            foreach (var tenant in tenants)
            {
                string fullName = $"{tenant.first_name} {tenant.last_name}";
                string email = string.IsNullOrEmpty(tenant.email) ? "No Email found" : tenant.email;

                List<string> doorNames = new List<string>();
                if (tenant.registered_doors != null)
                {
                    foreach (var doorId in tenant.registered_doors)
                    {
                        string doorName = await GetDoorNameById(doorId);
                        doorNames.Add(doorName);
                    }
                }

                string rooms = doorNames.Count > 0 ? string.Join(", ", doorNames) : "No rooms";

                dataGridViewTenant.Rows.Add(
                    tenant.id,
                    fullName,
                    email,
                    rooms
                );
            }
            dataGridViewTenant.ClearSelection();
        }

        // Show message when there are no tenants
        private void ShowEmptyMessage()
        {
            lblEmpty.Visible = true;
            lblEmpty.BringToFront();
            dataGridViewTenant.Rows.Clear();
        }

        // Set padding for DataGridView
        private void SetDataGridViewPadding()
        {
            int padding = 20;
            dataGridViewTenant.Location = new Point(padding, padding);
            dataGridViewTenant.Size = new Size(this.ClientSize.Width - (2 * padding), this.ClientSize.Height - (2 * padding));
        }

        // Event to handle resizing of the form
        protected override void OnResize(EventArgs e)
        {
            base.OnResize(e);
            SetDataGridViewPadding();
        }

        private async Task<string> GetDoorNameById(int doorId)
        {
            try
            {
                var response = await ApiService.httpClient.GetFromJsonAsync<DoorModel>($"door/{doorId}/");
                if (response != null && response.is_active && !response.is_deleted)
                {
                    return response.name;
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show($"Failed to fetch door details for ID {doorId}: {ex.Message}");
            }
            return "Unknown Door";
        }
    }
}
