using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace PiSync.Room.NewRoom
{
    public partial class NewRoomForm : Form
    {
        public NewRoomForm()
        {
            InitializeComponent();
        }

        private void btnCancel_Click(object sender, EventArgs e)
        {
            Hide();
        }

        private void btnSave_Click(object sender, EventArgs e)
        {
            var roomName = tbRoomName.Text.Trim();
            Console.WriteLine($"Room name: {roomName}");
            // saveToDatabase();
            Hide();
        }
    }
}
