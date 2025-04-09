import time
import requests
import RPi.GPIO as GPIO

# Configuration
IP_ADDRESS = '192.168.100.96'
DOOR_ID = 1
USERNAME = 'superuser'
DESCRIPTION = 'Updated via Raspberry Pi.'

OPEN_URL = f'http://{IP_ADDRESS}:8000/api/door/open/{DOOR_ID}/'
CLOSE_URL = f'http://{IP_ADDRESS}:8000/api/door/close/{DOOR_ID}/'
STATUS_URL = f'http://{IP_ADDRESS}:8000/api/doors/username/{USERNAME}/'

DOOR_PIN = 18

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(DOOR_PIN, GPIO.OUT)

def get_door_status():
    try:
        response = requests.get(STATUS_URL, timeout=5)
        if response.status_code == 200:
            data = response.json()
            return data['doors'][0]['status']  # Assumes only one door
    except requests.RequestException as e:
        print(f'Error fetching door status: {e}')
    return None

def send_door_action(open: bool):
    url = OPEN_URL if open else CLOSE_URL
    payload = {
        "username": USERNAME,
        "description": DESCRIPTION
    }
    try:
        response = requests.post(url, json=payload, timeout=5)
        if response.status_code == 200:
            print(f'Door {"opened" if open else "closed"} successfully.')
        else:
            print(f'Failed to {"open" if open else "close"} door: {response.status_code}')
    except requests.RequestException as e:
        print(f'Error sending door action: {e}')

def control_door():
    last_status = None
    while True:
        status = get_door_status()
        if status is not None and status != last_status:
            GPIO.output(DOOR_PIN, GPIO.HIGH if status else GPIO.LOW)
            send_door_action(open=status)
            print(f'DOOR is now {"OPEN" if status else "CLOSED"}')
            last_status = status
        else:
            print('No status change or failed to fetch status.')
        time.sleep(3)

if __name__ == '__main__':
    try:
        control_door()
    except KeyboardInterrupt:
        print('Exiting...')
    finally:
        GPIO.cleanup()
