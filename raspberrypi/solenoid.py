import time
import requests
from gpiozero import OutputDevice, Button
from lcd_utils import write_top
from threading import Thread

# Solenoid GPIO setup (ACTIVE-LOW relay)
SOLENOID_PIN = 17
solenoid = OutputDevice(SOLENOID_PIN, active_high=False, initial_value=True)

# Button GPIO setup
BUTTON_PIN = 18  # Button for 10s unlock (connected to API + solenoid)
button = Button(BUTTON_PIN)

# Key switch GPIO setup (manual override — not connected to API)
KEYSWITCH_PIN = 19  # Change this to your key switch pin
keyswitch = Button(KEYSWITCH_PIN)

# API endpoints
STATUS_URL = 'http://192.168.1.98:8000/api/door/status/1/'
CLOSE_URL = 'http://192.168.1.98:8000/api/door/close/1/'

# Track the last known state to avoid redundant switching
last_state = None

def unlock_solenoid():
    """Unlock the solenoid for 10 seconds"""
    print("🔓 Unlocking solenoid for 10 seconds...")
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

def monitor_button():
    """Monitor the button press and control the solenoid."""
    print('🚪 Button monitoring started.')
    while True:
        if button.is_pressed:
            write_top('Door opened')
            print("🔘 Button pressed. Unlocking door...")
            unlock_solenoid()
            time.sleep(1)  # Prevent multiple triggers while held
        time.sleep(0.1)

def monitor_api():
    """Monitor the door status from the API."""
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
                    last_state = False
                    print('🔒 Door closed via API.')
                    write_top('Door closed')
            else:
                print(f"⚠️ API error: {response.status_code}")
                write_top('Door error')
        except Exception as e:
            print(f"❌ Error checking status: {e}")
            write_top('Door error')

        time.sleep(3)

def monitor_keyswitch():
    """Monitor the key switch for manual override (no API involved)."""
    print('🔑 Key switch monitoring started.')
    override_active = False  # Track if override is active
    while True:
        if keyswitch.is_pressed and not override_active:
            solenoid.off()  # Unlock while key is turned
            write_top('Door opened (key)')
            print("🔓 Key turned: Solenoid unlocked.")
            override_active = True
        elif not keyswitch.is_pressed and override_active:
            solenoid.on()  # Lock back when key released
            write_top('Door closed (key)')
            print("🔒 Key released: Solenoid locked.")
            override_active = False
        time.sleep(0.1)

# Main function to run everything
if __name__ == "__main__":
    try:
        print("🔄 Solenoid monitoring started.")

        # Threads
        button_thread = Thread(target=monitor_button, daemon=True)
        button_thread.start()

        keyswitch_thread = Thread(target=monitor_keyswitch, daemon=True)
        keyswitch_thread.start()

        # API monitor stays in main thread
        monitor_api()

    except KeyboardInterrupt:
        print("\n🛑 Program terminated by user. Locking solenoid and exiting...")
        solenoid.on()
