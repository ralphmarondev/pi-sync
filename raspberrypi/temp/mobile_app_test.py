import time
import requests
import RPi.GPIO as GPIO

# Configuration
IP_ADDRESS = '192.168.1.99'  # Your server IP
DOOR_ID = 1
USERNAME = 'ralphmaron'
DESCRIPTION = 'Updated via Raspberry Pi.'

OPEN_URL = f'http://{IP_ADDRESS}:8000/api/door/open/{DOOR_ID}/'
CLOSE_URL = f'http://{IP_ADDRESS}:8000/api/door/close/{DOOR_ID}/'
STATUS_URL = f'http://{IP_ADDRESS}:8000/api/doors/username/{USERNAME}/'

RELAY_PIN = 17  # GPIO pin connected to the solenoid relay
GPIO.setmode(GPIO.BCM)
GPIO.setup(RELAY_PIN, GPIO.OUT)

# Default to LOCKED
GPIO.output(RELAY_PIN, GPIO.HIGH)

def get_door_status():
    try:
        response = requests.get(STATUS_URL, timeout=5)
        if response.status_code == 200:
            data = response.json()
            doors = data.get('doors', [])
            if doors:
                is_open = doors[0].get('is_open')
                print(f"📡 Door status from server: {'OPEN' if is_open else 'CLOSED'}")
                return is_open
    except requests.RequestException as e:
        print(f"⚠️ Network error: {e}")
    return None

def update_relay(is_open):
    # Solenoid is UNLOCKED (GPIO LOW) when door is open
    GPIO.output(RELAY_PIN, GPIO.LOW if is_open else GPIO.HIGH)
    print(f"{'🔓 UNLOCKED' if is_open else '🔒 LOCKED'} via GPIO")

def control_loop():
    last_status = None
    while True:
        current_status = get_door_status()
        if current_status is not None and current_status != last_status:
            update_relay(current_status)
            last_status = current_status
        time.sleep(3)

if __name__ == '__main__':
    try:
        print("📲 Waiting for app commands...")
        control_loop()
    except KeyboardInterrupt:
        print("👋 Shutting down.")
    finally:
        GPIO.output(RELAY_PIN, GPIO.HIGH)  # Ensure it's locked on exit
        GPIO.cleanup()
