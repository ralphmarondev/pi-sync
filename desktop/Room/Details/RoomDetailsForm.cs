using PiSync.Core.Model;

namespace PiSync.Room.Details
{
    public partial class RoomDetailsForm : Form
    {
        RoomModel room = new RoomModel();

        public RoomDetailsForm(int roomId, string roomName)
        {
            InitializeComponent();

            room.id = roomId;
            room.name = roomName;
        }
    }
}
