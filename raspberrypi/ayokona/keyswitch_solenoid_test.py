import time
from gpiozero import OutputDevice, Button

# Solenoid GPIO setup (ACTIVE-LOW relay)
SOLENOID_PIN = 17
solenoid = OutputDevice(SOLENOID_PIN, active_high=False, initial_value=True)

# Key switch setup (acts like button)
KEYSWITCH_PIN = 18  # Change this to your actual key switch pin
keyswitch = Button(KEYSWITCH_PIN)

def lock():
    solenoid.on()
    print("🔒 Solenoid locked.")

def unlock():
    solenoid.off()
    print("🔓 Solenoid unlocked.")

print("🔄 Solenoid + Keyswitch Test Started.")
print("Turn the key to unlock, release to lock.")

try:
    while True:
        if keyswitch.is_pressed:
            unlock()
        else:
            lock()
        time.sleep(0.1)  # Small delay to reduce CPU usage

except KeyboardInterrupt:
    print("\n🛑 Test stopped by user. Locking solenoid and exiting...")
    lock()
