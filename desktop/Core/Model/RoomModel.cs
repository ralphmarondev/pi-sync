using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PiSync.Core.Model
{
    public class RoomModel
    {
        public long id { get; set; }
        public string name { get; set; }
        public  bool isActive { get; set; }
        public bool isOpen { get; set; }
        public int tenantCount { get; set; }

        public RoomModel() { }
    }
}
