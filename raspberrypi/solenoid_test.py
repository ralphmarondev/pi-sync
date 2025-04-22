import RPi.GPIO as GPIO
import time

RELAY_PIN = 18  

# Setup
GPIO.setmode(GPIO.BCM)  # Use BCM numbering
GPIO.setup(RELAY_PIN, GPIO.OUT)

try:
    while True:
        print("Relay ON")
        GPIO.output(RELAY_PIN, GPIO.LOW)  
        time.sleep(2)

        print("Relay OFF")
        GPIO.output(RELAY_PIN, GPIO.HIGH) 
        time.sleep(2)

except KeyboardInterrupt:
    print("Exiting...")

finally:
    GPIO.output(RELAY_PIN, GPIO.HIGH)  
    GPIO.cleanup()