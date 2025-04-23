using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PiSync.Core.Network
{
    public class ApiService
    {
        private const string IP_ADDRESS = "192.168.1.99";
        public const string BASE_URL = $"http://{IP_ADDRESS}:8000/api/";
    }
}
