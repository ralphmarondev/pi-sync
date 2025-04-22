import RPi.GPIO as GPIO
import time

# Set the GPIO pin number (same as Arduino pin 7 equivalent)
RELAY_PIN = 7  # BCM numbering (not physical pin 7!)

# Setup
GPIO.setmode(GPIO.BCM)  # Use BCM numbering
GPIO.setup(RELAY_PIN, GPIO.OUT)

try:
    while True:
        print("Relay ON")
        GPIO.output(RELAY_PIN, GPIO.LOW)  # Active LOW: ON
        time.sleep(2)

        print("Relay OFF")
        GPIO.output(RELAY_PIN, GPIO.HIGH)  # OFF
        time.sleep(2)

except KeyboardInterrupt:
    print("Exiting...")

finally:
    GPIO.output(RELAY_PIN, GPIO.HIGH)  # Make sure it's off
    GPIO.cleanup()
