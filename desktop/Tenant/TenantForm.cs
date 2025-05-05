namespace PiSync.Tenant
{
    public partial class TenantForm : Form
    {
        public TenantForm()
        {
            InitializeComponent();
        }

        private void btnNewTenant_Click(object sender, EventArgs e)
        {
            NewTenantForm form = new NewTenantForm();
            form.ShowDialog(this);
        }
    }
}
