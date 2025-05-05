namespace PiSync.Tenant
{
    public partial class NewTenantForm : Form
    {
        public NewTenantForm()
        {
            InitializeComponent();
        }

        private void btnCancel_Click(object sender, EventArgs e)
        {
            Hide();
        }

        private void btnSave_Click(object sender, EventArgs e)
        {
            string firstName = tbFirstName.Text.Trim();
            string lastName = tbLastName.Text.Trim();
            string username = tbUsername.Text.Trim();
            string password = tbPassword.Text.Trim();
            string passwordHint = tbPasswordHint.Text.Trim();
            string gender = tbGender.Text.Trim();

            string registeredDoorText = tbRegisteredDoors.Text.Trim();
            List<string> registeredDoorList = registeredDoorText
                .Split(new char[] { ',' }, StringSplitOptions.RemoveEmptyEntries)
                .Select(s => s.Trim())
                .ToList();

            System.Diagnostics.Debug.WriteLine($"First name: `{firstName}`, Last name: `{lastName}`, username: `{username}`, password: `{password}`, passwordHint: `{passwordHint}`, gender: `{gender}`");
            System.Diagnostics.Debug.WriteLine($"Registered doors:");
            foreach (var item in registeredDoorList)
            {
                System.Diagnostics.Debug.WriteLine($"`{item}`");
            }

            if (string.IsNullOrEmpty(firstName))
            {
                ShowWarning("First name cannot be empty.");
                return;
            }
            if (string.IsNullOrEmpty(lastName))
            {
                ShowWarning("Last name cannot be empty.");
                return;
            }
            if (string.IsNullOrEmpty(username))
            {
                ShowWarning("Username cannot be empty.");
                return;
            }
            if (string.IsNullOrEmpty(gender))
            {
                ShowWarning("Gender cannot be empty.");
                return;
            }
            if (string.IsNullOrEmpty(password))
            {
                ShowWarning("Password cannot be empty.");
                return;
            }



        }

        private static void ShowWarning(string message)
        {
            MessageBox.Show(message, "Error", MessageBoxButtons.OK, MessageBoxIcon.Warning);
        }
    }
}
