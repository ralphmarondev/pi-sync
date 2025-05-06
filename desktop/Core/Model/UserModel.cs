namespace PiSync.Core.Model
{
    // UserModel.cs
    public class UserModel
    {
        public int id { get; set; }
        public List<int> registered_doors { get; set; }
        public string email { get; set; }
        public string username { get; set; }
        public string first_name { get; set; }
        public string last_name { get; set; }
        public string hint_password { get; set; }
        public bool is_superuser { get; set; }
        public string gender { get; set; }
        public DateTime create_date { get; set; }
        public string created_by { get; set; }
        public bool is_deleted { get; set; }
        public DateTime update_date { get; set; }
        public string image_url { get; set; }
    }

    // ApiResponse.cs
    public class ApiResponse<T>
    {
        public bool success { get; set; }
        public string message { get; set; }
        public T users { get; set; }
    }

    public class AuthResponse<T>
    {
        public bool success { get; set; }
        public string message { get; set; }
        public T user { get; set; }
    }
}
