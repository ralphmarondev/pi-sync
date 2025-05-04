import time
import serial
import threading
from gpiozero import OutputDevice
import adafruit_fingerprint

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
import serial
uart = serial.Serial("/dev/ttyUSB0", baudrate=57600, timeout=1)
finger = adafruit_fingerprint.Adafruit_Fingerprint(uart)

def get_fingerprint():
    """Get a fingerprint image, template it, and see if it matches!"""
    if finger.get_image() != adafruit_fingerprint.OK:
        return False
    if finger.image_2_tz(1) != adafruit_fingerprint.OK:
        return False
    if finger.finger_search() != adafruit_fingerprint.OK:
        return False
    return True

def auto_detect_loop():
    """Continuously check for valid fingerprint"""
    print("🟢 Auto fingerprint detection started.")
    while True:
        if get_fingerprint():
            print("✅ Detected ID #", finger.finger_id, "Confidence:", finger.confidence)
            unlock_solenoid()
            time.sleep(1)  # Avoid rapid repeated reads
        time.sleep(0.1)

def enroll_finger(location):
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
    i = -1
    while (i > max_number - 1) or (i < 0):
        try:
            i = int(input(f"Enter ID # from 0-{max_number - 1}: "))
        except ValueError:
            pass
    return i

# 🔁 Start background thread for auto-detection
threading.Thread(target=auto_detect_loop, daemon=True).start()

# Main menu loop for enrollment, deletion, etc.
while True:
    print("----------------")
    if finger.read_templates() != adafruit_fingerprint.OK:
        raise RuntimeError("Failed to read templates")
    print("Fingerprint templates: ", finger.templates)
    if finger.count_templates() != adafruit_fingerprint.OK:
        raise RuntimeError("Failed to read templates")
    print("Number of templates found: ", finger.template_count)
    if finger.read_sysparam() != adafruit_fingerprint.OK:
        raise RuntimeError("Failed to get system parameters")
    print("Size of template library: ", finger.library_size)
    print("e) enroll print")
    print("d) delete print")
    print("s) save fingerprint image")
    print("r) reset library")
    print("q) quit")
    print("----------------")
    c = input("> ")

    if c == "e":
        enroll_finger(get_num(finger.library_size))
    elif c == "d":
        if finger.delete_model(get_num(finger.library_size)) == adafruit_fingerprint.OK:
            print("Deleted!")
        else:
            print("Failed to delete")
    elif c == "s":
        save_fingerprint_image("fingerprint.png")
        print("Fingerprint image saved")
    elif c == "r":
        if finger.empty_library() == adafruit_fingerprint.OK:
            print("Library empty!")
        else:
            print("Failed to empty library")
    elif c == "q":
        print("Exiting fingerprint example program")
        break
