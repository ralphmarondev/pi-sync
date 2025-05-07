import time
import requests
from gpiozero import OutputDevice
from lcd_utils import write_top  # Import the LCD helper

# Solenoid GPIO setup (ACTIVE-LOW relay)
SOLENOID_PIN = 17
solenoid = OutputDevice(SOLENOID_PIN, active_high=False, initial_value=True)

# API endpoints
STATUS_URL = 'http://192.168.1.98:8000/api/door/status/1/'
CLOSE_URL = 'http://192.168.1.98:8000/api/door/close/1/'

# Track the last known state to avoid redundant switching
last_state = None

def unlock_solenoid():
    """Unlock the solenoid for 10 seconds"""
    write_top("🔓 Unlocking...")  # Update the top LCD with status
    print("🔓 Unlocking solenoid...")
    solenoid.off()
    time.sleep(10)
    solenoid.on()
    write_top("🔒 Locked again")  # Update the top LCD with status
    print("🔒 Solenoid locked again.")

    # Close on the API
    try:
        response = requests.post(CLOSE_URL, json={
            "description": "closed after 10s via solenoid auto-control"
        }, timeout=5)
        if response.status_code == 200:
            print("✅ API door closed successfully.")
        else:
            print(f"⚠️ Failed to close door on API: {response.status_code}")
    except Exception as e:
        print(f"❌ Error sending close request: {e}")

# Main loop
print("🔄 Solenoid monitoring started.")
try:
    while True:
        print('🌀 Checking door status from API...')
        try:
            response = requests.get(STATUS_URL, timeout=5)
            if response.status_code == 200:
                data = response.json()
                print("🔍 API response:", data)

                current_state = data.get('is_open', False)

                if current_state and last_state != True:
                    write_top("🚪 Door Opened")  # Update the top LCD with status
                    unlock_solenoid()
                    last_state = True
                elif not current_state:
                    write_top("🔒 Door Locked")  # Update the top LCD with status
                    last_state = False
            else:
                print(f"⚠️ API error: {response.status_code}")
                write_top("API Error")  # Update the top LCD with error
        except Exception as e:
            print(f"❌ Error checking status: {e}")
            write_top("Conn. Error")  # Update the top LCD with error

        time.sleep(3)

except KeyboardInterrupt:
    print("\n🛑 Program terminated by user.")
    solenoid.on()
    write_top("System stopped")  # Update the top LCD with status
