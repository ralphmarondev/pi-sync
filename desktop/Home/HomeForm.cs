namespace PiSync.Home
{
    public partial class HomeForm : Form
    {
        public HomeForm()
        {
            InitializeComponent();

            // open room form by default :>
            OpenRoomForm();
        }

        private void btnDashboard_Click(object sender, EventArgs e)
        {
            OpenDashboardForm();
        }

        private void btnRooms_Click(object sender, EventArgs e)
        {
            OpenRoomForm();
        }

        private void btnLogout_Click(object sender, EventArgs e)
        {
            AuthForm authForm = new AuthForm();
            Hide();
            authForm.ShowDialog();
        }

        #region NAVIGATION
        private void OpenFormInPanel(Form form)
        {
            mainPanel.Controls.Clear();

            form.TopLevel = false;
            form.FormBorderStyle = FormBorderStyle.None;
            form.Dock = DockStyle.Fill;
            mainPanel.Controls.Add(form);
            mainPanel.Tag = form;
            form.BringToFront();
            form.ShowInTaskbar = false;
            form.Show();
        }

        public void OpenDashboardForm()
        {
            OpenFormInPanel(new Dashboard.DashboardForm());
        }

        public void OpenRoomForm()
        {
            OpenFormInPanel(new Room.RoomForm());
        }

        private void btnHistory_Click(object sender, EventArgs e)
        {
            OpenFormInPanel(new History.HistoryForm());
        }
        #endregion NAVIGATION

        #region DRAG_AND_DROP
        private bool dragging = false;
        private Point dragCursorPoint;
        private Point dragFormPoint;

        private void OnMouseUp()
        {
            dragging = false;
        }

        private void OnMouseDown()
        {
            dragging = true;
            dragCursorPoint = Cursor.Position;
            dragFormPoint = this.Location;
        }

        private void OnMouseMove()
        {
            if (dragging)
            {
                Point diff = Point.Subtract(Cursor.Position, new Size(dragCursorPoint));
                this.Location = Point.Add(dragFormPoint, new Size(diff));
            }
        }
        #endregion DRAG_AND_DROP

        private void panelLabel_MouseUp(object sender, MouseEventArgs e)
        {
            OnMouseUp();
        }

        private void panelLabel_MouseMove(object sender, MouseEventArgs e)
        {
            OnMouseMove();
        }

        private void panelLabel_MouseDown(object sender, MouseEventArgs e)
        {
            OnMouseDown();
        }

        private void logoLabel_MouseUp(object sender, MouseEventArgs e)
        {
            OnMouseUp();
        }

        private void logoLabel_MouseMove(object sender, MouseEventArgs e)
        {
            OnMouseMove();
        }

        private void logoLabel_MouseDown(object sender, MouseEventArgs e)
        {
            OnMouseDown();
        }
    }
}
