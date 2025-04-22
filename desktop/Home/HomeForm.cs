using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

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

        public void OpenRoomForm()
        {
            OpenFormInPanel(new Room.RoomForm());
        }
        #endregion NAVIGATION
    }
}
