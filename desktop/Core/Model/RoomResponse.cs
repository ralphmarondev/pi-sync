using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PiSync.Core.Model
{
    public class RoomResponse
    {
        public bool Success { get; set; }
        public string Message { get; set; }
        public Door Door { get; set; }
    }

    public class Door
    {
        public int Id { get; set; }
        public string Name { get; set; }
        public bool IsActive { get; set; }
        public bool IsOpen { get; set; }
        public DateTime CreateDate { get; set; }
        public string CreatedBy { get; set; }
        public bool IsDeleted { get; set; }
        public DateTime UpdateDate { get; set; }
        public int TenantCount { get; set; }
    }

}
