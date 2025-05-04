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

            panel1.Location = new Point(5, 5);
            panel1.Size = new Size(this.Width, this.Height);
            this.Paint += DoorCardControl_Paint;
        }

        public void SetDoorInfo(int id, string name, string status, bool isOpen)
        {
            DoorId = id;
            DoorName = name;
            IsOpen = isOpen;

            lblDoorName.Text = name;
            lblDoorStatus.Text = status;

            this.Invalidate();
        }

        private void DoorCardControl_Click(object sender, EventArgs e)
        {
            DoorClicked?.Invoke(this, (DoorId, DoorName, IsOpen));
        }

        private void DoorCardControl_Paint(object sender, PaintEventArgs e)
        {
            Color borderColor = IsOpen ? Color.Green : Color.Red;
            int borderThickness = 4;

            using (Pen pen = new Pen(borderColor, borderThickness))
            {
                pen.Alignment = System.Drawing.Drawing2D.PenAlignment.Inset;
                e.Graphics.DrawRectangle(
                    pen,
                    borderThickness / 2,
                    borderThickness / 2,
                    this.Width - 1,
                    this.Height - 1
                );
            }
        }
    }
}
