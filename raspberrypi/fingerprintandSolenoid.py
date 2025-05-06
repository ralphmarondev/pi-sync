import time
import serial
import RPi.GPIO as GPIO
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

def enroll_finger(location):
    """Take two fingerprint images and template them, then store in 'location'"""
    for fingerimg in range(1, 3):
        if fingerimg == 1:
            print("Place finger on sensor...", end="")
        else:
            print("Place same finger again...", end="")

        while True:
            i = finger.get_image()
            if i == adafruit_fingerprint.OK:
                print("Image taken")
                break
            if i == adafruit_fingerprint.NOFINGER:
                print(".", end="")
            elif i == adafruit_fingerprint.IMAGEFAIL:
                print("Imaging error")
                return False
            else:
                print("Other error")
                return False

        print("Templating...", end="")
        i = finger.image_2_tz(fingerimg)
        if i == adafruit_fingerprint.OK:
            print("Templated")
        else:
            print("Template error")
            return False

        if fingerimg == 1:
            print("Remove finger")
            time.sleep(1)
            while finger.get_image() != adafruit_fingerprint.NOFINGER:
                pass

    print("Creating model...", end="")
    if finger.create_model() != adafruit_fingerprint.OK:
        print("Model creation failed")
        return False

    print("Storing model #%d..." % location, end="")
    if finger.store_model(location) == adafruit_fingerprint.OK:
        print("Stored")
        return True
    else:
        print("Failed to store")
        return False

def save_fingerprint_image(filename):
    """Scan fingerprint then save image to filename."""
    while finger.get_image():
        pass

    from PIL import Image
    img = Image.new("L", (256, 288), "white")
    pixeldata = img.load()
    mask = 0b00001111
    result = finger.get_fpdata(sensorbuffer="image")

    x = 0
    y = 0
    for i in range(len(result)):
        pixeldata[x, y] = (int(result[i]) >> 4) * 17
        x += 1
        pixeldata[x, y] = (int(result[i]) & mask) * 17
        if x == 255:
            x = 0
            y += 1
        else:
            x += 1

    img.save(filename)

def get_num(max_number):
    """Get a valid number from 0 to max_number."""
    i = -1
    while (i > max_number - 1) or (i < 0):
        try:
            i = int(input(f"Enter ID # from 0-{max_number - 1}: "))
        except ValueError:
            pass
    return i

# --- AUTO-DETECT FINGERPRINT LOOP ---

print("Starting automatic fingerprint detection...")

if finger.read_templates() != adafruit_fingerprint.OK:
    raise RuntimeError("Failed to read templates")

while True:
    if finger.get_image() == adafruit_fingerprint.OK:
        if finger.image_2_tz(1) == adafruit_fingerprint.OK:
            if finger.finger_search() == adafruit_fingerprint.OK:
                print("Authorized fingerprint detected!")
                print("ID #", finger.finger_id, "with confidence", finger.confidence)
                unlock_solenoid()
                # Wait until finger is removed to prevent duplicate unlocks
                while finger.get_image() != adafruit_fingerprint.NOFINGER:
                    time.sleep(0.1)
            else:
                print("Unauthorized fingerprint.")
                # Optional: wait for finger to be removed
                while finger.get_image() != adafruit_fingerprint.NOFINGER:
                    time.sleep(0.1)
    time.sleep(0.1)  # Small delay to avoid high CPU usage
