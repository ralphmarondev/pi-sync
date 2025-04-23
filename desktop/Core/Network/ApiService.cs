using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PiSync.Core.Network
{
    public class ApiService
    {
        public static readonly string configPath = "config.txt";
        public static readonly string BASE_URL = $"http://{LoadIPAddress()}:8000/api/";

        private static string LoadIPAddress()
        {
            if (!File.Exists(configPath))
            {
                // default ip if not found
                File.WriteAllText(configPath, "192.168.1.99");
            }

            return File.ReadAllText(configPath).Trim();
        }
    }
}
