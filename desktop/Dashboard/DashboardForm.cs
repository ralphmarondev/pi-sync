using System.Net.Http.Json;
using PiSync.Core.Model;
using PiSync.Core.Network;
using PiSync.Home;

namespace PiSync.Dashboard
{
    public partial class DashboardForm : Form
    {
        public DashboardForm()
        {
            InitializeComponent();
        }

        private void DashboardForm_Load(object sender, EventArgs e)
        {
            PopulateDoorsAsync();
        }

        private async Task<List<RoomModel>> FetchRoomsAsync()
        {
            try
            {
                var response = await ApiService.httpClient.GetFromJsonAsync<List<RoomModel>>("doors/");
                return response ?? new List<RoomModel>();
            }
            catch (Exception ex)
            {
                MessageBox.Show($"Error fetching rooms: {ex.Message}", "API Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return new List<RoomModel>();
            }
        }


        private async Task PopulateDoorsAsync()
        {
            panelRooms.Controls.Clear();

            var rooms = await FetchRoomsAsync();

            foreach (var room in rooms)
            {
                var doorCard = new DoorCardControl();

                string statusText = room.isOpen ? "Open" : "Closed";

                doorCard.SetDoorInfo(Convert.ToInt32(room.id), room.name, statusText, room.isOpen);
                doorCard.DoorClicked += DoorCard_DoorClicked;

                doorCard.Margin = new Padding(10);
                doorCard.Width = 150;
                doorCard.Height = 150;

                panelRooms.Controls.Add(doorCard);
            }
        }

        private async void DoorCard_DoorClicked(object sender, (int doorId, string doorName, bool isOpen) doorInfo)
        {
            //MessageBox.Show($"Clicked door: {doorInfo.doorName}", "Door Clicked", MessageBoxButtons.OK, MessageBoxIcon.Information);
            System.Diagnostics.Debug.WriteLine($"Clicked door: {doorInfo.doorName}");

            var (doorId, doorName, isOpen) = doorInfo;
            bool shouldOpen = !isOpen;

            await SendDoorActionAsync(doorId, shouldOpen);
            await PopulateDoorsAsync();
        }

        private async Task SendDoorActionAsync(int doorId, bool open)
        {
            var body = new
            {
                usernname = "admin",
                description = open ? "Opened via dashboard" : "Closed via dashboard"
            };
            string endpoint = open ? $"door/open/{doorId}/" : $"door/close/{doorId}/";

            try
            {
                var response = await ApiService.httpClient.PostAsJsonAsync(endpoint, body);
                response.EnsureSuccessStatusCode();

                //MessageBox.Show($"Door {(open ? "opened" : "closed")} successfully!", "Success", MessageBoxButtons.OK, MessageBoxIcon.Information);
                System.Diagnostics.Debug.WriteLine($"Door {(open ? "opened" : "closed")} successfully!");
            }
            catch (Exception ex)
            {
                MessageBox.Show($"Failed to {(open ? "open" : "close")} door: {ex.Message}", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }

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

        private void panel1_MouseUp(object sender, MouseEventArgs e)
        {
            OnMouseUp();
        }

        private void panel1_MouseMove(object sender, MouseEventArgs e)
        {
            OnMouseMove();
        }

        private void panel1_MouseDown(object sender, MouseEventArgs e)
        {
            OnMouseDown();
        }

    }
}
