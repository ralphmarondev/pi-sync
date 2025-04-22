import RPi.GPIO as GPIO
import time

relay_pin = 17  # Change this to your GPIO pin

GPIO.setmode(GPIO.BCM)
GPIO.setup(relay_pin, GPIO.OUT)

while True:
    GPIO.output(relay_pin, GPIO.LOW)  # Should turn OFF the relay (green LED off)
    print("Relay OFF")
    time.sleep(5)
    
    GPIO.output(relay_pin, GPIO.HIGH)   # Should turn ON the relay (green LED on)
    print("Relay ON")
    time.sleep(5)
