namespace PiSync.Tenant
{
    public partial class TenantManageForm : Form
    {
        private int tenantId;
        private string tenantName;
        public TenantManageForm(int tenantId, string tenantName)
        {
            InitializeComponent();

            this.tenantId = tenantId;
            this.tenantName = tenantName;

            System.Diagnostics.Debug.WriteLine($"Tenant id: {tenantId}, tenant name: {tenantName}");
        }
    }
}
