using System;
using System.Collections.Generic;
using System.Drawing;
using System.Net.Http;
using System.Text.Json;
using System.Threading.Tasks;
using System.Windows.Forms;
using PiSync.Core.Model;

namespace PiSync.Room
{
    public partial class RoomForm : Form
    {
        private List<RoomModel> rooms = new List<RoomModel>();
        private readonly HttpClient httpClient = new HttpClient { BaseAddress = new Uri("http://192.168.68.129:8000/api/") };

        public RoomForm()
        {
            InitializeComponent();
            SetupDataGridView();
            _ = FetchRoomsAsync();
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
        }

        private async Task FetchRoomsAsync()
        {
            try
            {
                var response = await httpClient.GetAsync("doors");
                if (response.IsSuccessStatusCode)
                {
                    string jsonString = await response.Content.ReadAsStringAsync();
                    rooms = JsonSerializer.Deserialize<List<RoomModel>>(jsonString);
                    PopulateRooms();
                }
                else
                {
                    string error = await response.Content.ReadAsStringAsync();
                    MessageBox.Show($"Failed to fetch rooms: {error}");
                    ShowEmptyMessage();
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show($"Exception occurred while fetching rooms: {ex.Message}");
                ShowEmptyMessage();
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
                // Show detail view here later
            }
        }

        #endregion
    }
}
