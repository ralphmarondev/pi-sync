using PiSync.Core.Model;
using PiSync.Core.Network;
using PiSync.Home;
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
        public DashboardForm()
        {
            InitializeComponent();
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
