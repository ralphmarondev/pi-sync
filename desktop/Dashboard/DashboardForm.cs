﻿using System.Net.Http.Json;
using PiSync.Admin;
using PiSync.Core.Model;
using PiSync.Core.Network;
using PiSync.Core.Utils;
using PiSync.Home;

namespace PiSync.Dashboard
{
    public partial class DashboardForm : Form
    {
        private System.Windows.Forms.Timer refreshTimer;
        public DashboardForm()
        {
            InitializeComponent();

            btnAdminName.Text = SessionManager.FullName;
        }

        private void DashboardForm_Load(object sender, EventArgs e)
        {
            PopulateDoorsAsync();

            refreshTimer = new System.Windows.Forms.Timer();
            refreshTimer.Interval = 3000;
            refreshTimer.Tick += async (s, args) => await PopulateDoorsAsync();
            refreshTimer.Start();
        }

        private void DashboardForm_FormClosed(object sender, FormClosedEventArgs e)
        {
            refreshTimer?.Stop();
            refreshTimer?.Dispose();
            base.OnFormClosed(e);
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
            var sortedRooms = rooms.OrderBy(r => r.name).ToList();
            foreach (var room in sortedRooms)
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

            bool isAllowed = await IsAdminAccessAllowedAsync(doorId);
            if (!isAllowed)
            {
                MessageBox.Show($"You are not allowed to open/close '{doorName}' as admin access is disabled by tenant.", "Access denied", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                return;
            }
            
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

        private async Task<bool> IsAdminAccessAllowedAsync(int doorId)
        {
            try
            {
                var response = await ApiService.httpClient.GetFromJsonAsync<AdminAccessResponse>($"door/admin-access/{doorId}/");
                return response?.allow_admin_access ?? false;
            }
            catch (Exception ex)
            {
                MessageBox.Show($"Failed to check admin access: {ex.Message}", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return false;
            }
        }

        private class AdminAccessResponse
        {
            public bool success { get; set; }
            public bool allow_admin_access { get; set; }
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

        private void lblTitle_MouseMove(object sender, MouseEventArgs e)
        {
            OnMouseMove();
        }

        private void lblTitle_MouseUp(object sender, MouseEventArgs e)
        {
            OnMouseUp();
        }

        private void lblTitle_MouseDown(object sender, MouseEventArgs e)
        {
            OnMouseDown();
        }

        private void btnFullScreen_Click(object sender, EventArgs e)
        {
            HomeForm mainForm = ParentForm as HomeForm;

            if (mainForm != null)
            {
                mainForm.ToggleFullScreen();
            }
        }

        private void btnAdminName_Click(object sender, EventArgs e)
        {
            AdminForm adminForm = new AdminForm();

            adminForm.ShowDialog(this);
        }

        private void btnAdminName_MouseMove(object sender, MouseEventArgs e)
        {
            OnMouseMove();
        }

        private void btnAdminName_MouseUp(object sender, MouseEventArgs e)
        {
            OnMouseUp();
        }

        private void btnAdminName_MouseDown(object sender, MouseEventArgs e)
        {
            OnMouseDown();
        }

        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            OnMouseMove();
        }

        private void pictureBox1_MouseUp(object sender, MouseEventArgs e)
        {
            OnMouseUp();
        }

        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            OnMouseDown();
        }
    }
}
