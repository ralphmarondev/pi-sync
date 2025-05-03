using System.Net.Http.Json;
using PiSync.Core.Model;
using PiSync.Core.Network;
using PiSync.Home;
using PiSync.Room.NewRoom;

namespace PiSync.Room
{
    public partial class RoomForm : Form
    {
        private List<RoomModel> rooms = new List<RoomModel>();
        private readonly HttpClient httpClient = new HttpClient { BaseAddress = new Uri(ApiService.BASE_URL) };
        private readonly System.Windows.Forms.Timer refreshTimer = new System.Windows.Forms.Timer();

        public RoomForm()
        {
            InitializeComponent();
            SetupDataGridView();
            FetchRoomsAsync();

            // Timer for auto-refresh every 3 seconds
            refreshTimer.Interval = 3000;
            refreshTimer.Tick += (s, e) => FetchRoomsAsync();
            refreshTimer.Start();
        }

        #region DATAGRIDVIEW_SETUP_AND_FETCHING

        private void SetupDataGridView()
        {
            dataGridViewRooms.Columns.Clear();

            dataGridViewRooms.Columns.Add("id", "ID");
            dataGridViewRooms.Columns["id"].Visible = false;

            dataGridViewRooms.Columns.Add("name", "Name");
            dataGridViewRooms.Columns.Add("tenantCount", "Tenant Count");
            dataGridViewRooms.Columns.Add("status", "Status"); // isOpen: Open/Closed
            dataGridViewRooms.Columns.Add("isActive", "Active Status"); // New column

            dataGridViewRooms.AutoSizeColumnsMode = DataGridViewAutoSizeColumnsMode.Fill;
            dataGridViewRooms.ReadOnly = true;
            dataGridViewRooms.AllowUserToAddRows = false;
            dataGridViewRooms.AllowUserToDeleteRows = false;
            dataGridViewRooms.RowTemplate.Height = 60;
            dataGridViewRooms.DefaultCellStyle.WrapMode = DataGridViewTriState.True;

            dataGridViewRooms.DefaultCellStyle.Font = new Font("Courier New", 14);
            dataGridViewRooms.ColumnHeadersDefaultCellStyle.Font = new Font("Courier New", 14, FontStyle.Bold);
            dataGridViewRooms.ColumnHeadersDefaultCellStyle.ForeColor = Color.Purple;
            dataGridViewRooms.EnableHeadersVisualStyles = false;

            SetDataGridViewPadding();
        }

        private async void FetchRoomsAsync()
        {
            try
            {
                var response = await httpClient.GetFromJsonAsync<List<RoomModel>>("doors/");
                if (response != null)
                {
                    rooms = response;
                    PopulateRooms();
                }
                else
                {
                    ShowEmptyMessage();
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show($"Failed to fetch rooms: {ex.Message}");
            }
        }

        private void PopulateRooms()
        {
            lblEmpty.Visible = rooms.Count == 0;
            dataGridViewRooms.Rows.Clear();

            foreach (var room in rooms)
            {
                dataGridViewRooms.Rows.Add(
                    room.id,
                    room.name,
                    room.tenantCount,
                    room.isOpen ? "Open" : "Closed",
                    room.isActive ? "Active" : "Inactive"
                );
            }
        }

        private void ShowEmptyMessage()
        {
            lblEmpty.Visible = true;
            lblEmpty.BringToFront();
            dataGridViewRooms.Rows.Clear();
        }

        private void SetDataGridViewPadding()
        {
            int padding = 20;
            dataGridViewRooms.Location = new Point(padding, padding);
            dataGridViewRooms.Size = new Size(this.ClientSize.Width - (2 * padding), this.ClientSize.Height - (2 * padding));
        }

        protected override void OnResize(EventArgs e)
        {
            base.OnResize(e);
            SetDataGridViewPadding();
        }

        protected override void OnFormClosed(FormClosedEventArgs e)
        {
            refreshTimer.Stop();
            base.OnFormClosed(e);
        }

        #endregion



        #region DRAG_AND_DROP
        private bool dragging = false;
        private Point dragCursorPoint;
        private Point dragFormPoint;

        private void OnMouseUp()
        {
            dragging = false;
        }

        private void OnMouseMove()
        {
            if (dragging)
            {
                Point diff = Point.Subtract(Cursor.Position, new Size(dragCursorPoint));
                HomeForm mainScreen = this.ParentForm as HomeForm;

                if (mainScreen != null)
                {
                    mainScreen.Location = Point.Add(dragFormPoint, new Size(diff));
                }
            }
        }

        private void OnMouseDown()
        {
            dragging = true;
            dragCursorPoint = Cursor.Position;
            dragFormPoint = this.ParentForm.Location;
        }
        #endregion DRAG_AND_DROP



        private void panelTopbar_MouseUp(object sender, MouseEventArgs e)
        {
            OnMouseUp();
        }

        private void panelTopbar_MouseMove(object sender, MouseEventArgs e)
        {
            OnMouseMove();
        }

        private void panelTopbar_MouseDown(object sender, MouseEventArgs e)
        {
            OnMouseDown();
        }

        private void btnNewRoom_Click(object sender, EventArgs e)
        {
            var newRoomForm = new NewRoomForm();

            newRoomForm.ShowDialog(this);
        }
    }
}
