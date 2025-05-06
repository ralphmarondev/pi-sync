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


        private void TenantManageForm_Load(object sender, EventArgs e)
        {
            OpenFormInPanel(new Details.TenantDetailsForm(tenantId, tenantName));
        }

        private void OpenFormInPanel(Form form)
        {
            panelContent.Controls.Clear();

            form.TopLevel = false;
            form.FormBorderStyle = FormBorderStyle.None;
            form.Dock = DockStyle.Fill;
            panelContent.Controls.Add(form);
            panelContent.Tag = form;
            form.BringToFront();
            form.ShowInTaskbar = false;
            form.Show();
        }

        private void btnDetails_Click(object sender, EventArgs e)
        {
            OpenFormInPanel(new Details.TenantDetailsForm(tenantId, tenantName));
        }

        private void btnUpdate_Click(object sender, EventArgs e)
        {

        }

        private void btnDelete_Click(object sender, EventArgs e)
        {
            OpenFormInPanel(new Delete.TenantDeleteForm(tenantId, tenantName));
        }

        private void btnClose_Click(object sender, EventArgs e)
        {
            Hide();
        }
    }
}
