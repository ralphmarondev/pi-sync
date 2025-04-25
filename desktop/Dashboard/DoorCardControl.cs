using PiSync.Core.Model;
using System;
using System.Drawing;
using System.Net.Http.Json;
using System.Windows.Forms;

namespace PiSync.Dashboard
{
    public partial class DoorCardControl : UserControl
    {
        public DoorCardControl()
        {
            InitializeComponent();
        }

        public void SetDoorInfo(string name, string status)
        {
            lblDoorName.Text = name;
            lblDoorStatus.Text = status;
        }
    }
}
