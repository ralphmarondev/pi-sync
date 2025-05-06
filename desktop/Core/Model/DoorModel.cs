using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PiSync.Core.Model
{
    public class DoorModel
    {
        public int id { get; set; }
        public string name { get; set; }
        public bool is_active { get; set; }
        public bool is_open { get; set; }
        public DateTime create_date { get; set; }
        public string created_by { get; set; }
        public bool is_deleted { get; set; }
        public DateTime update_date { get; set; }
        public int tenant_count { get; set; }
    }

}
