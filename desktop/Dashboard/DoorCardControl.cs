namespace PiSync.Dashboard
{
    public partial class DoorCardControl : UserControl
    {
        public int DoorId { get; private set; }
        public string DoorName { get; private set; }
        public bool IsOpen { get; private set; }

        public event EventHandler<(int doorId, string doorName, bool isOpen)> DoorClicked;

        public DoorCardControl()
        {
            InitializeComponent();
            this.Click += DoorCardControl_Click;

            foreach (Control ctrl in this.Controls)
            {
                ctrl.Click += DoorCardControl_Click;
            }
        }

        public void SetDoorInfo(int id, string name, string status, bool isOpen)
        {
            DoorId = id;
            DoorName = name;
            IsOpen = isOpen;

            lblDoorName.Text = name;
            lblDoorStatus.Text = status;
        }

        private void DoorCardControl_Click(object sender, EventArgs e)
        {
            DoorClicked?.Invoke(this, (DoorId, DoorName, IsOpen));
        }
    }
}
