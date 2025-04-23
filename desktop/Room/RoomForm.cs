using System;
using System.Collections.Generic;
using System.Drawing;
using System.Net.Http;
using System.Net.Http.Json;
using System.Windows.Forms;
using PiSync.Core.Model;
using PiSync.Core.Network;

namespace PiSync.Room
{
    public partial class RoomForm : Form
    {
        private List<RoomModel> rooms = new List<RoomModel>();
        private readonly HttpClient httpClient = new HttpClient { BaseAddress = new Uri(ApiService.BASE_URL) };

        public RoomForm()
        {
            InitializeComponent();
            SetupDataGridView();
            FetchRoomsAsync();
        }

        #region POPULATING_DATAGRIDVIEW

        private void SetupDataGridView()
        {
            dataGridViewRooms.Columns.Clear();
            
            dataGridViewRooms.Columns.Add("id", "ID");
            dataGridViewRooms.Columns["id"].Visible = false;

            dataGridViewRooms.Columns.Add("name", "Name");
            dataGridViewRooms.Columns.Add("tenantCount", "Tenants");
            dataGridViewRooms.Columns.Add("status", "Status");

            DataGridViewButtonColumn actionColumn = new DataGridViewButtonColumn();
            actionColumn.Name = "Action";
            actionColumn.Text = "More";
            actionColumn.UseColumnTextForButtonValue = true;
            dataGridViewRooms.Columns.Add(actionColumn);

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

            dataGridViewRooms.CellClick += dataGridViewRooms_CellContentClick;

            // Set initial position and size with margin
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
                    room.isOpen ? "Open" : "Closed"
                );
            }
        }

        private void ShowEmptyMessage()
        {
            lblEmpty.Visible = true;
            lblEmpty.BringToFront();
            dataGridViewRooms.Rows.Clear();
        }

        private void dataGridViewRooms_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {
            if (e.RowIndex >= 0 && e.ColumnIndex == dataGridViewRooms.Columns["Action"].Index)
            {
                string id = dataGridViewRooms.Rows[e.RowIndex].Cells["id"].Value.ToString();
                Console.WriteLine($"Room ID clicked: {id}");
                // You can show a detail modal here later
            }
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

        #endregion
    }
}
