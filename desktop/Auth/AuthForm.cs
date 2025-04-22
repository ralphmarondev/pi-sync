using PiSync.Home;

namespace PiSync
{
    public partial class AuthForm : Form
    {
        public AuthForm()
        {
            InitializeComponent();
        }

        private bool isValid(string username, string password)
        {
            try
            {
                return (username == "ralphmaron" && password == "iscute");
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Error: {ex.Message}");
            }
            return false;
        }

        private void btnLogin_Click(object sender, EventArgs e)
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

            if (isValid(username, password))
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
