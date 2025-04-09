import time
import requests
import RPi.GPIO as GPIO

# Configuration
IP_ADDRESS = '192.168.100.96'
API_URL = f'http://{IP_ADDRESS}:8000/api/door/open/1/'
DOOR_PIN = 18

# Set up the GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(DOOR_PIN, GPIO.OUT)

def get_door_status():
    try:
      response = requests.get(API_URL, timeout=5)
      if response.status_code == 200:
          data = response.json()
          return data['status']
    except requests.RequestException as e:
        print(f'Error fetching DOOR status: {e}')
    return None

def control_door():
    while True:
        status = get_door_status()
        if status is not None:
            GPIO.output(DOOR_PIN, GPIO.HIGH if status else GPIO.LOW)
            print(f'DOOR status: {"OPEN" if status else "CLOSED"}')
        else:
            print('Failed to fetch DOOR status')
        time.sleep(2)

if __name__ == '__main__':
    try:
        control_door()
    except KeyboardInterrupt:
        print('Exiting...')
    finally:
        GPIO.cleanup()