import time
import requests
from gpiozero import OutputDevice, Button
from lcd_utils import write_top

# Solenoid GPIO setup (ACTIVE-LOW relay)
SOLENOID_PIN = 17
solenoid = OutputDevice(SOLENOID_PIN, active_high=False, initial_value=True)

# Button GPIO setup
BUTTON_PIN = 18  # Change this to your actual button pin
button = Button(BUTTON_PIN)

# API endpoints
STATUS_URL = 'http://192.168.1.98:8000/api/door/status/1/'
OPEN_URL = 'http://192.168.1.98:8000/api/door/open/1/'
CLOSE_URL = 'http://192.168.1.98:8000/api/door/close/1/'

# Track the last known state to avoid redundant switching
last_state = None

def unlock_solenoid():
    """Unlock the solenoid for 10 seconds"""
    print("🔓 Unlocking solenoid...")
    solenoid.off()
    write_top('Door opened')
    time.sleep(10)
    solenoid.on()
    write_top('Door closed')
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

def press_button_trigger_api():
    """Send an open door request to the API when button is pressed."""
    print("🔘 Button pressed! Sending open request to API...")
    try:
        response = requests.post(OPEN_URL, json={
            "description": "opened via physical button press"
        }, timeout=5)
        if response.status_code == 200:
            print("✅ Door open request sent successfully.")
        else:
            print(f"⚠️ Failed to open door on API: {response.status_code}")
    except Exception as e:
        print(f"❌ Error sending open request: {e}")

def monitor_button():
    """Monitor the button press and send open request to API."""
    print('🚪 Button monitoring started.')
    while True:
        if button.is_pressed:
            press_button_trigger_api()
            time.sleep(1)  # Prevent multiple rapid requests while button is held
        time.sleep(0.1)  # Small delay to avoid overloading the CPU

def monitor_api():
    """Monitor the door status from the API and control solenoid."""
    global last_state
    while True:
        print('🌀 Checking door status from API...')
        try:
            response = requests.get(STATUS_URL, timeout=5)
            if response.status_code == 200:
                data = response.json()
                print("🔍 API response:", data)

                current_state = data.get('is_open', False)

                if current_state and last_state != True:
                    unlock_solenoid()
                    print('✅ Door opened via API.')
                    write_top('Door opened')
                    last_state = True
                elif not current_state and last_state != False:
                    last_state = False  # Reset state tracking
                    print('🔒 Door closed via API.')
                    write_top('Door closed')
            else:
                print(f"⚠️ API error: {response.status_code}")
                write_top('Door error')
        except Exception as e:
            print(f"❌ Error checking status: {e}")
            write_top('Door error')

        time.sleep(3)

# Main function to run both button monitoring and API status checking
if __name__ == "__main__":
    try:
        print("🔄 Solenoid monitoring started.")
        from threading import Thread
        
        # Start the button monitoring in a separate thread
        button_thread = Thread(target=monitor_button, daemon=True)
        button_thread.start()

        # Start the API monitoring in the main thread
        monitor_api()

    except KeyboardInterrupt:
        print("\n🛑 Program terminated by user.")
        solenoid.on()  # Ensure it's locked on exit
