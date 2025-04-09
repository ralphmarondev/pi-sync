import time
import requests
import RPi.GPIO as GPIO

# Configuration
IP_ADDRESS = '192.168.100.96'
DOOR_ID = 1
USERNAME = 'ralphmaron'
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
            doors = data.get('doors', [])
            if doors:
                status = doors[0].get('status')
                print(f"Fetched door status: {'OPEN' if status else 'CLOSED'}")
                return status
            else:
                print("No doors found in response.")
        else:
            print(f"Error: Received unexpected status code {response.status_code}")
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
            print(f'Door {"opened" if open else "closed"} successfully via API.')
        else:
            print(f'Failed to send door {"open" if open else "close"} request: {response.status_code}')
    except requests.RequestException as e:
        print(f'Error sending door action: {e}')

def control_door():
    last_status = None
    while True:
        status = get_door_status()
        print(f'Getting status: {status}')
        if status is not None:
            if status != last_status:
                GPIO.output(DOOR_PIN, GPIO.HIGH if status else GPIO.LOW)
                send_door_action(open=status)
                print(f'Door is now {"OPEN" if status else "CLOSED"}')
                last_status = status
            else:
                print("No change in door status.")
        else:
            print("Failed to get valid door status.")
        time.sleep(3)

if __name__ == '__main__':
    try:
        print('Raspberry pi started...')
        control_door()
    except KeyboardInterrupt:
        print('Exiting...')
    finally:
        GPIO.cleanup()
