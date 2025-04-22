using System.Text;
using System.Text.Json;
using System.Threading.Tasks;
using PiSync.Home;

namespace PiSync
{
    public partial class AuthForm : Form
    {
        private readonly HttpClient httpClient = new HttpClient();
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

                var response = await httpClient.PostAsync("http://192.168.68.129:8000/api/login/", content);

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
                var home= new HomeForm();
                this.Hide();
                home.Show();
            }
            else
            {
                MessageBox.Show("Invalid credentials.");
            }
        }

        private void btnForgotPassword_LinkClicked(object sender, LinkLabelLinkClickedEventArgs e)
        {
            MessageBox.Show("No hint available.");
        }
    }
}
