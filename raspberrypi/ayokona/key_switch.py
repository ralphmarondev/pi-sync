import time
from gpiozero import OutputDevice, Button
from lcd_utils import write_top

# Solenoid GPIO setup (ACTIVE-LOW relay)
SOLENOID_PIN = 17
solenoid = OutputDevice(SOLENOID_PIN, active_high=False, initial_value=True)

# Key switch GPIO setup
KEYSWITCH_PIN = 23  # Use an available GPIO pin for your key switch
key_switch = Button(KEYSWITCH_PIN)

def manual_unlock():
    """Physically unlock the solenoid when key switch is turned."""
    print("🔑 Key switch activated! Unlocking solenoid...")
    solenoid.off()
    write_top('Manual open')
    time.sleep(10)  # Keep it open for 10 seconds
    solenoid.on()
    write_top('Door closed')
    print("🔒 Solenoid locked again after manual override.")

def monitor_key_switch():
    """Monitor key switch and unlock door on activation."""
    print('🔄 Key switch manual override monitoring started.')
    while True:
        if key_switch.is_pressed:
            manual_unlock()
            time.sleep(1)  # Debounce delay
        time.sleep(0.1)

if __name__ == "__main__":
    try:
        monitor_key_switch()
    except KeyboardInterrupt:
        print("\n🛑 Manual override stopped by user.")
        solenoid.on()
