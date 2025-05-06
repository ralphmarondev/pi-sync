import time
import serial
import adafruit_fingerprint
from gpiozero import OutputDevice

# Set up GPIO for controlling the solenoid (ACTIVE-LOW relay)
SOLENOID_PIN = 17
solenoid = OutputDevice(SOLENOID_PIN, active_high=False, initial_value=True)

def unlock_solenoid():
    """Unlock the solenoid (activate relay)"""
    print("Unlocking the solenoid...")
    solenoid.on()   # GPIO LOW → relay ON → solenoid unlocked
    time.sleep(5)
    solenoid.off()  # GPIO HIGH → relay OFF → solenoid locked
    print("Solenoid locked again.")

# Initialize serial connection to the fingerprint sensor
uart = serial.Serial("/dev/ttyUSB0", baudrate=57600, timeout=1)
finger = adafruit_fingerprint.Adafruit_Fingerprint(uart)

# Start auto-detection loop
print("Starting automatic fingerprint detection...")

# Read templates to verify connection and existing prints
if finger.read_templates() != adafruit_fingerprint.OK:
    raise RuntimeError("Failed to read fingerprint templates.")

# Main loop: constantly wait for fingerprint
while True:
    if finger.get_image() == adafruit_fingerprint.OK:
        if finger.image_2_tz(1) == adafruit_fingerprint.OK:
            if finger.finger_search() == adafruit_fingerprint.OK:
                print("✅ Authorized fingerprint detected!")
                print("User ID #", finger.finger_id, "Confidence:", finger.confidence)
                unlock_solenoid()
                # Wait until finger is removed to avoid repeat scans
                while finger.get_image() != adafruit_fingerprint.NOFINGER:
                    time.sleep(0.1)
            else:
                print("❌ Unauthorized fingerprint.")
                # Wait until finger is removed
                while finger.get_image() != adafruit_fingerprint.NOFINGER:
                    time.sleep(0.1)
    time.sleep(0.1)  # Short delay to prevent high CPU usage
