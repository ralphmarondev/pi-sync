namespace PiSync.Dashboard
{
    public partial class DoorCardControl : UserControl
    {
        public string DoorName { get; private set; }
        public event EventHandler<string> DoorClicked;

        public DoorCardControl()
        {
            InitializeComponent();
            this.Click += DoorCardControl_Click;

            foreach (Control ctrl in this.Controls)
            {
                ctrl.Click += DoorCardControl_Click;
            }
        }

        public void SetDoorInfo(string name, string status)
        {
            DoorName = name;
            lblDoorName.Text = name;
            lblDoorStatus.Text = status;
        }

        private void DoorCardControl_Click(object sender, EventArgs e)
        {
            DoorClicked?.Invoke(this, DoorName);
        }
    }
}
