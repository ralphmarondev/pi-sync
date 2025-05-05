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
        }
    }
}
