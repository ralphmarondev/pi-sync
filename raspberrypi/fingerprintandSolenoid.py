import time
import serial
import adafruit_fingerprint
from gpiozero import OutputDevice
import threading

# Set up GPIO for solenoid (ACTIVE-LOW relay logic)
SOLENOID_PIN = 17
solenoid = OutputDevice(SOLENOID_PIN, active_high=False, initial_value=True)

def unlock_solenoid():
    """Unlock the solenoid (activate relay)"""
    print("🔓 Unlocking solenoid...")
    solenoid.off()  # GPIO LOW → relay ON → solenoid unlocked
    time.sleep(10)  # Keep it unlocked for 10 seconds
    solenoid.on()   # GPIO HIGH → relay OFF → solenoid locked
    print("🔒 Solenoid locked again.")

# Initialize fingerprint sensor
uart = serial.Serial("/dev/ttyUSB0", baudrate=57600, timeout=1)
finger = adafruit_fingerprint.Adafruit_Fingerprint(uart)

def enroll_finger(location):
    """Enroll a fingerprint into specified location"""
    for fingerimg in range(1, 3):
        if fingerimg == 1:
            print("➡️ Place finger on sensor and hold it still.")
        else:
            print("➡️ Place the SAME finger again.")

        start_time = time.time()
        timeout = 20  # Allow up to 20 seconds for user to place finger

        while time.time() - start_time < timeout:
            i = finger.get_image()
            if i == adafruit_fingerprint.OK:
                print("✅ Image taken.")
                break
            elif i == adafruit_fingerprint.NOFINGER:
                print(".", end="", flush=True)
                time.sleep(0.5)
            elif i == adafruit_fingerprint.IMAGEFAIL:
                print("\n❌ Imaging error.")
                return False
            else:
                print("\n❌ Unknown error.")
                return False
        else:
            print("\n⏱️ Timeout: No finger detected in time.")
            return False

        print("Templating...", end="")
        i = finger.image_2_tz(fingerimg)
        if i == adafruit_fingerprint.OK:
            print("✅ Templated.")
        else:
            print("❌ Template error.")
            return False

        if fingerimg == 1:
            print("✋ Remove finger.")
            time.sleep(2)
            remove_start = time.time()
            while finger.get_image() != adafruit_fingerprint.NOFINGER:
                if time.time() - remove_start > 10:
                    print("⚠️ Finger not removed in time.")
                    return False
                time.sleep(0.1)

    print("🧠 Creating model...", end="")
    if finger.create_model() != adafruit_fingerprint.OK:
        print("❌ Model creation failed.")
        return False

    print(f"💾 Storing model #{location}...", end="")
    if finger.store_model(location) == adafruit_fingerprint.OK:
        print("✅ Stored successfully.")
        return True
    else:
        print("❌ Failed to store fingerprint.")
        return False

def get_num(max_number):
    """Get a valid fingerprint ID number from user."""
    i = -1
    while (i < 0) or (i > max_number - 1):
        try:
            i = int(input(f"Enter ID # (0 to {max_number - 1}): "))
        except ValueError:
            pass
    return i

# -------- Background Detection Thread --------
def auto_detect_loop():
    while True:
        if finger.get_image() == adafruit_fingerprint.OK:
            if finger.image_2_tz(1) == adafruit_fingerprint.OK:
                if finger.finger_search() == adafruit_fingerprint.OK:
                    print("✅ Authorized fingerprint detected!")
                    print("ID #", finger.finger_id, "Confidence:", finger.confidence)
                    unlock_solenoid()
                    while finger.get_image() != adafruit_fingerprint.NOFINGER:
                        time.sleep(0.1)
                else:
                    print("❌ Unauthorized fingerprint.")
                    while finger.get_image() != adafruit_fingerprint.NOFINGER:
                        time.sleep(0.1)
        time.sleep(0.1)

# -------- Main Program --------
print("📦 Fingerprint system ready.")
print("Press Ctrl+C to exit at any time.")

if finger.read_templates() != adafruit_fingerprint.OK:
    raise RuntimeError("❌ Failed to read fingerprint templates.")
if finger.count_templates() != adafruit_fingerprint.OK:
    raise RuntimeError("❌ Failed to count templates.")

# Start background thread
threading.Thread(target=auto_detect_loop, daemon=True).start()

# Menu loop
while True:
    print("\nMenu Options:")
    print("e) Enroll fingerprint")
    print("q) Quit")
    choice = input("Select option: ").lower()

    if choice == "e":
        location = get_num(finger.library_size)
        enroll_finger(location)
    elif choice == "q":
        print("👋 Exiting program.")
        break
    else:
        print("❓ Invalid option. Try again.")
