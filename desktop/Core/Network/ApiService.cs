namespace PiSync.Core.Network
{
    public class ApiService
    {
        public static readonly string configPath = "cute.config.txt";
        public static readonly string BASE_URL = $"http://{LoadIPAddress()}:8000/api/";
        public static readonly HttpClient httpClient = CreateHttpClient();

        private static string LoadIPAddress()
        {
            try
            {
                if (!File.Exists(configPath))
                {
                    return "";
                }

                var ip = File.ReadAllText(configPath).Trim();
                if (string.IsNullOrEmpty(ip))
                {
                    return "";
                }
                System.Diagnostics.Debug.WriteLine($"Ip address: {ip}");
                return ip;
            }
            catch
            {
                return "";
            }
        }

        private static HttpClient CreateHttpClient()
        {
            var client = new HttpClient();

            if (!string.IsNullOrWhiteSpace(BASE_URL))
            {
                client.BaseAddress = new Uri(BASE_URL);
            }
            return client;
        }
    }
}
