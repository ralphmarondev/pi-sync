import time
from gpiozero import OutputDevice

# Solenoid GPIO setup (ACTIVE-LOW relay)
SOLENOID_PIN = 17
solenoid = OutputDevice(SOLENOID_PIN, active_high=False, initial_value=True)

print("🔄 Solenoid test started. It will open and close every 5 seconds.")

try:
    while True:
        print("🔓 Opening solenoid...")
        solenoid.off()  # Activate relay (solenoid opens)
        time.sleep(5)

        print("🔒 Closing solenoid...")
        solenoid.on()  # Deactivate relay (solenoid closes)
        time.sleep(5)

except KeyboardInterrupt:
    print("\n🛑 Test stopped by user.")
    solenoid.on()  # Ensure it's locked on exit
