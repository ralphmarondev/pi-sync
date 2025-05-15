using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PiSync.Core.Helpers
{
    using System.Net.Http.Json;
    using PiSync.Core.Model;
    using PiSync.Core.Network;

    public static class RoomHelper
    {
        public static async Task<List<int>?> ParseRoomNamesToIdsAsync(string commaSeparatedRoomNames)
        {
            if (string.IsNullOrWhiteSpace(commaSeparatedRoomNames))
                return new List<int>();

            List<int> doorIds = new List<int>();
            var doorNames = commaSeparatedRoomNames
                .Split(new[] { ',' }, StringSplitOptions.RemoveEmptyEntries)
                .Select(name => name.Trim());

            foreach (var doorName in doorNames)
            {
                try
                {
                    var response = await ApiService.httpClient.GetAsync($"door/name/{doorName}/");
                    if (response.IsSuccessStatusCode)
                    {
                        var room = await response.Content.ReadFromJsonAsync<RoomResponse>();
                        if (room?.Door != null)
                        {
                            doorIds.Add(room.Door.Id);
                        }
                        else
                        {
                            System.Diagnostics.Debug.WriteLine($"Room `{doorName}` not found in response.");
                            return null;
                        }
                    }
                    else
                    {
                        string error = await response.Content.ReadAsStringAsync();
                        System.Diagnostics.Debug.WriteLine($"Failed to fetch room `{doorName}`. {error}");
                        return null;
                    }
                }
                catch (Exception ex)
                {
                    System.Diagnostics.Debug.WriteLine($"Exception while parsing room `{doorName}`: {ex.Message}");
                    return null;
                }
            }

            return doorIds;
        }
    }

}
