using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Text.Json.Serialization;
using System.Threading.Tasks;

namespace PiSync.Core.Model
{
    public class RoomModel
    {
        [JsonPropertyName("id")]
        public long id { get; set; }

        [JsonPropertyName("name")]
        public string name { get; set; }

        [JsonPropertyName("is_active")]
        public  bool isActive { get; set; }

        [JsonPropertyName("is_open")]
        public bool isOpen { get; set; }

        [JsonPropertyName("tenant_count")]
        public int tenantCount { get; set; }

        public RoomModel() { }
    }
}
