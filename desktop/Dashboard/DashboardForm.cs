using PiSync.Core.Model;
using PiSync.Core.Network;
using System;
using System.Collections.Generic;
using System.Drawing;
using System.Net.Http;
using System.Net.Http.Json;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace PiSync.Dashboard
{
    public partial class DashboardForm : Form
    {
        private readonly HttpClient httpClient = new HttpClient { BaseAddress = new Uri(ApiService.BASE_URL) };
        private readonly System.Windows.Forms.Timer refreshTimer = new System.Windows.Forms.Timer();

        // Keep track of door controls by ID
        private Dictionary<long, DoorCardControl> doorControls = new();

        public DashboardForm()
        {
            InitializeComponent();
            InitDashboard();
            StartRefresh();
        }

        private void InitDashboard()
        {
            this.BackColor = Color.White;

            // Assuming you have a panel named "panelRooms" on your form
            panelRooms.AutoScroll = true;
            panelRooms.Padding = new Padding(20);
            //panelRooms.FlowDirection = FlowDirection.LeftToRight;
            //panelRooms.WrapContents = true;
        }

        private void StartRefresh()
        {
            refreshTimer.Interval = 3000;
            refreshTimer.Tick += async (s, e) => await FetchAndUpdateDoors();
            refreshTimer.Start();
        }

        private async Task FetchAndUpdateDoors()
        {
            try
            {
                var doors = await httpClient.GetFromJsonAsync<List<RoomModel>>("doors/");
                if (doors == null) return;

                foreach (var door in doors)
                {
                    if (doorControls.ContainsKey(door.id))
                    {
                        // Update existing card
                        doorControls[door.id].SetData(door);
                    }
                    else
                    {
                        // Create new card
                        var card = new DoorCardControl();
                        card.SetData(door);
                        panelRooms.Controls.Add(card); // Add card to existing panel
                        doorControls[door.id] = card;
                    }
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine("Failed to fetch doors: " + ex.Message);
            }
        }
    }
}
