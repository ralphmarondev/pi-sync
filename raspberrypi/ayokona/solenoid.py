import time
import requests
from gpiozero import OutputDevice

# Solenoid GPIO setup (ACTIVE-LOW relay)
SOLENOID_PIN = 17
solenoid = OutputDevice(SOLENOID_PIN, active_high=False, initial_value=True)

# API endpoint
STATUS_URL = 'http://192.168.1.98:8000/api/door/status/1/'

# Track the last known state to avoid redundant switching
last_state = None

def unlock_solenoid():
    """Unlock the solenoid for 10 seconds"""
    print("🔓 Unlocking solenoid...")
    solenoid.off()
    time.sleep(10)
    solenoid.on()
    print("🔒 Solenoid locked again.")

# Main loop
print("🔄 Solenoid monitoring started.")
try:
    while True:
        try:
            response = requests.get(STATUS_URL, timeout=5)
            if response.status_code == 200:
                data = response.json()
                current_state = data.get('state', False)

                if current_state and last_state != True:
                    unlock_solenoid()
                    last_state = True
                elif not current_state:
                    last_state = False  # Reset state tracking
            else:
                print(f"⚠️ API error: {response.status_code}")
        except Exception as e:
            print(f"❌ Error checking status: {e}")

        time.sleep(3)

except KeyboardInterrupt:
    print("\n🛑 Program terminated by user.")
