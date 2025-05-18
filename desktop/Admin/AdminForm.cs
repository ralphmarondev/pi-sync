using System.Net.Http.Json;
using PiSync.Core.Model;
using PiSync.Core.Network;
using PiSync.Core.Utils;

namespace PiSync.Admin
{
    public partial class AdminForm : Form
    {
        private AdminUpdateMessage admin;
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

    }
}
