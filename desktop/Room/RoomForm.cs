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
        private readonly System.Windows.Forms.Timer refreshTimer;

        public RoomForm()
        {
            InitializeComponent();
            SetupDataGridView();
            FetchRoomsAsync();

            // Timer for auto-refresh
            refreshTimer = new System.Windows.Forms.Timer();
            refreshTimer.Interval = 10000;
            refreshTimer.Tick += (s, e) => FetchRoomsAsync();
            refreshTimer.Start();
        }


        private void RoomForm_FormClosed(object sender, FormClosedEventArgs e)
        {
            refreshTimer?.Stop();
            refreshTimer?.Dispose();
            base.OnFormClosed(e);
        }
        #region DATAGRIDVIEW_SETUP_AND_FETCHING

        private void SetupDataGridView()
        {
            dataGridViewRooms.Columns.Clear();
            dataGridViewRooms.SelectionMode = DataGridViewSelectionMode.FullRowSelect;

            dataGridViewRooms.Columns.Add("id", "ID");
            dataGridViewRooms.Columns["id"].Visible = false;

            dataGridViewRooms.Columns.Add("name", "Name");
            dataGridViewRooms.Columns.Add("tenantCount", "Tenant Count");
            dataGridViewRooms.Columns.Add("status", "Door Status"); // isOpen: Open/Closed
            dataGridViewRooms.Columns.Add("isActive", "Room Status"); // New column

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

            dataGridViewRooms.CellClick += DataGridViewRooms_CellClick;
            dataGridViewRooms.MultiSelect = false;
            dataGridViewRooms.Cursor = Cursors.Hand;

            SetDataGridViewPadding();
        }

        private async void FetchRoomsAsync()
        {
            try
            {
                var response = await ApiService.httpClient.GetFromJsonAsync<List<RoomModel>>("doors/");
                if (response != null)
                {
                    rooms = response;
                    PopulateRooms();
                    dataGridViewRooms.ClearSelection();
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
            dataGridViewRooms.ClearSelection();
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

        private void DataGridViewRooms_CellClick(object sender, DataGridViewCellEventArgs e)
        {
            // Ignore clicks on header
            if (e.RowIndex < 0)
            {
                return;
            }

            var selectedRow = dataGridViewRooms.Rows[e.RowIndex];

            var roomId = Convert.ToInt32(selectedRow.Cells["id"].Value);
            var roomName = selectedRow.Cells["name"].Value.ToString();

            System.Diagnostics.Debug.WriteLine($"Clicked room id: {roomId}, Name: {roomName}");

            RoomManageForm form = new RoomManageForm(roomId, roomName);
            form.ShowDialog(this);
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
