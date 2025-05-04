namespace PiSync.Core.Model
{
    public class HistoryModel
    {
        public int id { get; set; }
        public string room_name { get; set; }
        public string username { get; set; }
        public string description { get; set; }
        public DateTime timestamp { get; set; }
        public int room { get; set; }
    }
}
