import RPi.GPIO as GPIO 
from time import sleep 

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

while True:
    GPIO.output(18, 1)
    sleep(2)
    GPIO.output(18, 0)
    sleep(2)
