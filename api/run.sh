#!/bin/bash

# NOTE: THIS IS FOR LINUX
# Get the IP address of the current machine
# This uses `hostname -I` to get the IP address; adjust if needed (for macOS, use `ipconfig getifaddr en0`)

# uncomment if on linux :)
# IP_ADDRESS=$(hostname -I | awk '{print $1}') 

# Explanation:
# - hostname -I: Returns all IP addresses assigned to your machine.
# - awk '{print $1}': Picks the first IP address which should be your local IP.
# END FOR LINUX

# NOTE: FOR WINDOWS
# Get the IP address of the current machine using `ipconfig` and filter it for the active network interface
IP_ADDRESS=$(ipconfig | grep -A 10 "Wireless LAN adapter Wi-Fi" | grep "IPv4 Address" | awk '{print $NF}')

# Explanation:
# - ipconfig: Returns all network information.
# - grep "Wireless LAN adapter Wi-Fi": Filters the output for the Wi-Fi adapter (adjust if you're using Ethernet).
# - grep "IPv4 Address": Finds the line containing the IP address.
# - awk '{print $NF}': Prints the last field, which is the IP address.


# Explanation for the user:
# Running Django on 0.0.0.0 makes the server accessible on any IP address on your network.
# You are setting the host to 0.0.0.0 and port to 8000 for external access.

echo "Running Django development server on: https://$IP_ADDRESS:8000"

# Explanation:
# This command runs the Django server, making it available on all interfaces (0.0.0.0)
# Port 8000 is the default port, but you can change it if needed.
python manage.py runsslserver --certificate certs/cert.pem --key certs/key.pem 0.0.0.0:8000

# To stop the server, press CTRL+C in the terminal where it's running.


