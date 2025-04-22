import RPi.GPIO as GPIO
import time

# Constants
RELAY_PIN = 17  # GPIO pin connected to relay IN

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(RELAY_PIN, GPIO.OUT)
GPIO.output(RELAY_PIN, GPIO.LOW)  

# Track current state
is_unlocked = False

def toggle_solenoid():
    global is_unlocked
    if is_unlocked:
        # Lock it
        GPIO.output(RELAY_PIN, GPIO.LOW)
        print("🔒 Solenoid is now LOCKED.")
    else:
        # Unlock it
        GPIO.output(RELAY_PIN, GPIO.HIGH)
        print("🔓 Solenoid is now UNLOCKED.")
    is_unlocked = not is_unlocked

try:
    print("Press Ctrl+C to exit.")
    while True:
        input("Press ENTER to toggle solenoid...")
        toggle_solenoid()

except KeyboardInterrupt:
    print("\nExiting...")

finally:
    GPIO.output(RELAY_PIN, GPIO.HIGH)  # Ensure it's locked on exit
    GPIO.cleanup()
