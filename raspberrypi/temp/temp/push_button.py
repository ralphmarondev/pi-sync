import time
from gpiozero import OutputDevice, Button
from lcd_utils import write_top

# Solenoid GPIO setup (ACTIVE-LOW relay)
SOLENOID_PIN = 17
solenoid = OutputDevice(SOLENOID_PIN, active_high=False, initial_value=True)

# Button GPIO setup
BUTTON_PIN = 18  # Change this to your actual button pin
button = Button(BUTTON_PIN)

def unlock_solenoid():
    """Unlock the solenoid for 10 seconds"""
    print("🔓 Unlocking solenoid...")
    solenoid.off()
    write_top('Door opened')
    time.sleep(10)
    solenoid.on()
    write_top('Door closed')
    print("🔒 Solenoid locked again.")

def monitor_button():
    """Monitor the button press and control the solenoid."""
    while True:
        if button.is_pressed:
            print("Button pressed. Unlocking door...")
            unlock_solenoid()
        time.sleep(0.1)  # Small delay to avoid overloading the CPU

# Main function to run the button monitoring
if __name__ == "__main__":
    try:
        print("🔄 Solenoid test started.")
        # Start the button monitoring
        monitor_button()

    except KeyboardInterrupt:
        print("\n🛑 Program terminated by user.")
        solenoid.on()  # Ensure it's locked on exit
