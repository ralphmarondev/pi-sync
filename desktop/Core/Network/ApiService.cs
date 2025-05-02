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
            var TRIESHA_BOARDING_IP = "192.168.1.98";
            var BOARDING_IP = "192.168.68.118";

            Console.WriteLine($"{TRIESHA_BOARDING_IP}, {BOARDING_IP}");

            if (!File.Exists(configPath))
            {
                // default ip if not found
                File.WriteAllText(configPath, "192.168.1.98");
            }

            //return File.ReadAllText(configPath).Trim();
            return BOARDING_IP;
        }
    }
}
