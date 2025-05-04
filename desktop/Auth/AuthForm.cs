using System.Net.Http.Json;
using System.Text;
using System.Text.Json;
using PiSync.Core.Model;
using PiSync.Core.Network;
using PiSync.Home;

namespace PiSync
{
    public partial class AuthForm : Form
    {
        public AuthForm()
        {
            InitializeComponent();
        }

        private async Task<bool> isValid(string username, string password)
        {
            try
            {
                var loginData = new
                {
                    username = username,
                    password = password
                };
                string json = JsonSerializer.Serialize(loginData);
                var content = new StringContent(json, Encoding.UTF8, "application/json");

                var response = await ApiService.httpClient.PostAsync($"{ApiService.BASE_URL}login/", content);

                if (response.IsSuccessStatusCode)
                {
                    string result = await response.Content.ReadAsStringAsync();
                    Console.WriteLine($"Server response: {result}");
                    return true;
                }
                else
                {
                    string error = await response.Content.ReadAsStringAsync();
                    Console.WriteLine($"Login failed: {error}");
                    return false;
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Error: {ex.Message}");
            }
            return false;
        }

        private async void btnLogin_Click(object sender, EventArgs e)
        {
            string username = tbUsername.Text.Trim();
            string password = tbPassword.Text.Trim();

            Console.WriteLine($"Username: {username}, password: {password}");

            if (username == string.Empty && password == string.Empty)
            {
                MessageBox.Show("Username and password cannot be empty!");
                return;
            }

            if (username == string.Empty)
            {
                MessageBox.Show("Username cannot be empty!");
                return;
            }
            if (password == string.Empty)
            {
                MessageBox.Show("Password cannot be empty!");
                return;
            }

            btnLogin.Enabled = false;
            btnLogin.Text = "Logging in...";
            var isAuthenticated = await isValid(username, password);
            btnLogin.Enabled = true;
            btnLogin.Text = "Login";

            if (isAuthenticated)
            {
                MessageBox.Show("Login successful.");
                var home = new HomeForm();
                this.Hide();
                home.Show();
            }
            else
            {
                MessageBox.Show("Invalid credentials.");
            }
        }

        private async void btnForgotPassword_LinkClicked(object sender, LinkLabelLinkClickedEventArgs e)
        {
            string username = tbUsername.Text.Trim();

            if (string.IsNullOrEmpty(username))
            {
                MessageBox.Show("Username is empty!", "Information", MessageBoxButtons.OK, MessageBoxIcon.Information);
                tbUsername.Focus();
                return;
            }

            try
            {
                string url = $"user/password-hint/{username}/";
                var response = await ApiService.httpClient.GetFromJsonAsync<PasswordHintResponse>(url);

                if (response != null && response.success && !string.IsNullOrEmpty(response.password_hint))
                {
                    MessageBox.Show($"{response.password_hint}", "Password Hint", MessageBoxButtons.OK, MessageBoxIcon.Information);
                }
                else
                {
                    MessageBox.Show("No hint available.", "Password Hint", MessageBoxButtons.OK, MessageBoxIcon.Information);
                }
            }
            catch (Exception ex)
            {
                System.Diagnostics.Debug.WriteLine($"Error: {ex.Message}");
                MessageBox.Show("No hint available.", "Password Hint", MessageBoxButtons.OK, MessageBoxIcon.Information);
            }
        }


        #region DRAG_AND_DROP
        private bool dragging = false;
        private Point dragCursorPoint;
        private Point dragFormPoint;

        private void OnMouseUp()
        {
            dragging = false;
        }

        private void OnMouseDown()
        {
            dragging = true;
            dragCursorPoint = Cursor.Position;
            dragFormPoint = this.Location;
        }

        private void OnMouseMove()
        {
            if (dragging)
            {
                Point diff = Point.Subtract(Cursor.Position, new Size(dragCursorPoint));
                this.Location = Point.Add(dragFormPoint, new Size(diff));
            }
        }
        #endregion DRAG_AND_DROP

        private void panelAuth_MouseUp(object sender, MouseEventArgs e)
        {
            OnMouseUp();
        }

        private void panelAuth_MouseMove(object sender, MouseEventArgs e)
        {
            OnMouseMove();
        }

        private void panelAuth_MouseDown(object sender, MouseEventArgs e)
        {
            OnMouseDown();
        }

        private void lblTitle_MouseUp(object sender, MouseEventArgs e)
        {
            OnMouseUp();
        }

        private void lblTitle_MouseMove(object sender, MouseEventArgs e)
        {
            OnMouseMove();
        }

        private void lblTitle_MouseDown(object sender, MouseEventArgs e)
        {
            OnMouseDown();
        }

        private void btnClose_Click(object sender, EventArgs e)
        {
            Close();
        }

        private void btnSetupIp_Click(object sender, EventArgs e)
        {
            string ipAddress = Microsoft.VisualBasic.Interaction.InputBox(
                "Enter the IP Address!",
                "Setup IP Address",
                "192.168.1.1");

            if (string.IsNullOrWhiteSpace(ipAddress))
            {
                MessageBox.Show("IP Address setup canceled or invalid", "Info", MessageBoxButtons.OK, MessageBoxIcon.Information);
                return;
            }

            try
            {
                string filePath = Path.Combine(AppDomain.CurrentDomain.BaseDirectory, "cute.config.txt");

                File.WriteAllText(filePath, ipAddress);
                MessageBox.Show($"IP Address saved to cute.config.txt\n\n{ipAddress}", "Success", MessageBoxButtons.OK, MessageBoxIcon.Information);

            }
            catch (Exception ex)
            {
                MessageBox.Show($"Failed to save IP Address.\n\n{ex.Message}", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }
    }
}
