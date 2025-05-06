using System.Text.Json.Serialization;

namespace PiSync.Core.Model
{
    public class RegisterTenantRequest
    {
        [JsonPropertyName("username")]
        public string Username { get; set; }

        [JsonPropertyName("first_name")]
        public string FirstName { get; set; }

        [JsonPropertyName("last_name")]
        public string LastName { get; set; }

        [JsonPropertyName("password")]
        public string Password { get; set; }

        [JsonPropertyName("hint_password")]
        public string HintPassword { get; set; }

        [JsonPropertyName("gender")]
        public string Gender { get; set; }

        [JsonPropertyName("registered_doors")]
        public List<int> RegisteredDoors { get; set; }
    }

}
