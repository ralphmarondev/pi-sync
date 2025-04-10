import RPi.GPIO as GPIO 
from time import sleep 

DOOR_PIN = 23

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(DOOR_PIN, GPIO.OUT)

while True:
    print('Opening solenoid...')
    GPIO.output(DOOR_PIN, 1)
    sleep(1)
    print('Closing solenoid...')
    GPIO.output(DOOR_PIN, 0)
    sleep(1)
