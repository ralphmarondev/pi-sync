using System.Net.Http.Json;
using PiSync.Core.Model;
using PiSync.Core.Network;
using PiSync.Home;

namespace PiSync.History
{
    public partial class HistoryForm : Form
    {
        private List<HistoryModel> historyRecords = new List<HistoryModel>();

        public HistoryForm()
        {
            InitializeComponent();
            SetupDataGridView();
            FetchHistoryAsync();
        }

        #region DATAGRIDVIEW_SETUP_AND_FETCHING

        private void SetupDataGridView()
        {
            dataGridViewHistory.Columns.Clear();
            dataGridViewHistory.SelectionMode = DataGridViewSelectionMode.FullRowSelect;

            dataGridViewHistory.Columns.Add("description", "Description");
            dataGridViewHistory.Columns.Add("room_name", "Room");
            dataGridViewHistory.Columns.Add("username", "Username");
            dataGridViewHistory.Columns.Add("timestamp", "Date");

            dataGridViewHistory.AutoSizeColumnsMode = DataGridViewAutoSizeColumnsMode.Fill;
            dataGridViewHistory.ReadOnly = true;
            dataGridViewHistory.AllowUserToAddRows = false;
            dataGridViewHistory.AllowUserToDeleteRows = false;
            dataGridViewHistory.RowTemplate.Height = 50;
            dataGridViewHistory.DefaultCellStyle.WrapMode = DataGridViewTriState.True;

            dataGridViewHistory.DefaultCellStyle.Font = new Font("Courier New", 12);
            dataGridViewHistory.ColumnHeadersDefaultCellStyle.Font = new Font("Courier New", 12, FontStyle.Bold);
            dataGridViewHistory.ColumnHeadersDefaultCellStyle.ForeColor = Color.Purple;
            dataGridViewHistory.EnableHeadersVisualStyles = false;

            dataGridViewHistory.MultiSelect = false;
            dataGridViewHistory.Cursor = Cursors.Hand;
        }

        private async void FetchHistoryAsync()
        {
            try
            {
                var response = await ApiService.httpClient.GetFromJsonAsync<List<HistoryModel>>("history/");
                if (response != null)
                {
                    historyRecords = response;
                    PopulateHistory();
                    dataGridViewHistory.ClearSelection();
                }
                else
                {
                    ShowEmptyMessage();
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show($"Failed to fetch history: {ex.Message}");
            }
        }

        private void PopulateHistory()
        {
            lblEmpty.Visible = historyRecords.Count == 0;
            dataGridViewHistory.Rows.Clear();

            var sortedHistory = historyRecords.OrderByDescending(h => h.timestamp).ToList();

            foreach (var record in sortedHistory)
            {
                dataGridViewHistory.Rows.Add(
                    record.description,
                    record.room_name,
                    record.username,
                    record.timestamp.ToLocalTime().ToString("yyyy-MM-dd HH:mm:ss")
                );
            }
            dataGridViewHistory.ClearSelection();
        }

        private void ShowEmptyMessage()
        {
            lblEmpty.Visible = true;
            lblEmpty.BringToFront();
            dataGridViewHistory.Rows.Clear();
        }

        #endregion


        private void tbSearch_TextChanged(object sender, EventArgs e)
        {
            string searchText = tbSearch.Text.Trim().ToLower();

            if (string.IsNullOrEmpty(searchText))
            {
                PopulateHistory();
            }
            else
            {
                var filteredHistory = historyRecords
                    .Where(h =>
                        (h.room_name != null && h.room_name.ToLower().Contains(searchText)) ||
                        (h.username != null && h.username.ToLower().Contains(searchText)) ||
                        (h.description != null && h.description.ToLower().Contains(searchText))
                    )
                    .OrderByDescending(h => h.timestamp)
                    .ToList();

                lblEmpty.Visible = filteredHistory.Count == 0;
                dataGridViewHistory.Rows.Clear();

                foreach (var record in filteredHistory)
                {
                    dataGridViewHistory.Rows.Add(
                        record.description,
                        record.room_name,
                        record.username,
                        record.timestamp.ToLocalTime().ToString("yyyy-MM-dd HH:mm:ss")
                    );
                }

                dataGridViewHistory.ClearSelection();
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


        private void panel1_MouseMove(object sender, MouseEventArgs e)
        {
            OnMouseMove();
        }

        private void panel1_MouseUp(object sender, MouseEventArgs e)
        {
            OnMouseUp();
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
    }
}
