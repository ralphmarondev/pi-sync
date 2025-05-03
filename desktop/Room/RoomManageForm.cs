using PiSync.Core.Model;

namespace PiSync.Room
{
    public partial class RoomManageForm : Form
    {
        RoomModel room = new RoomModel();
        public RoomManageForm(int roomId, string roomName)
        {
            InitializeComponent();

            room.id = roomId;
            room.name = roomName;
        }

        private void RoomManageForm_Load(object sender, EventArgs e)
        {
            System.Diagnostics.Debug.WriteLine($"Name: {room.name}, id: {room.id}");

            OpenFormInPanel(new Details.RoomDetailsForm(Convert.ToInt32(room.id), room.name));
        }

        private void OpenFormInPanel(Form form)
        {
            panelContent.Controls.Clear();

            form.TopLevel = false;
            form.FormBorderStyle = FormBorderStyle.None;
            form.Dock = DockStyle.Fill;
            panelContent.Controls.Add(form);
            panelContent.Tag = form;
            form.BringToFront();
            form.ShowInTaskbar = false;
            form.Show();
        }

        private void btnDetails_Click(object sender, EventArgs e)
        {

        }
    }
}
