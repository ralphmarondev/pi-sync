using PiSync.Core.Model;

namespace PiSync.Room.Details
{
    public partial class RoomDetailsForm : Form
    {
        RoomModel room = new RoomModel();
        public RoomDetailsForm()
        {
            InitializeComponent();
        }

        public RoomDetailsForm(int roomId, string roomName)
        {
            InitializeComponent();

            room.id = roomId;
            room.name = roomName;

            label1.Text = $"Name: {room.name}, id: {room.id}";
        }
    }
}
