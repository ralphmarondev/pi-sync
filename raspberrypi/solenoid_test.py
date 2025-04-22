import RPi.GPIO as GPIO
import os

RELAY_PIN = 17  # GPIO pin connected to relay IN
STATE_FILE = "lock_state.txt"

# Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(RELAY_PIN, GPIO.OUT)

def read_state():
    if not os.path.exists(STATE_FILE):
        return "locked"  # Default state
    with open(STATE_FILE, "r") as f:
        return f.read().strip()

def write_state(state):
    with open(STATE_FILE, "w") as f:
        f.write(state)

def switch_solenoid():
    current_state = read_state()

    if current_state == "locked":
        # Unlock
        GPIO.output(RELAY_PIN, GPIO.LOW)  # Active LOW → unlock
        write_state("unlocked")
        print("🔓 Solenoid UNLOCKED")
    else:
        # Lock
        GPIO.output(RELAY_PIN, GPIO.HIGH)  # Relay OFF → lock
        write_state("locked")
        print("🔒 Solenoid LOCKED")

if __name__ == "__main__":
    try:
        switch_solenoid()
    finally:
        GPIO.cleanup()
import RPi.GPIO as GPIO
import os

RELAY_PIN = 17  # GPIO pin connected to relay IN
STATE_FILE = "lock_state.txt"

# Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(RELAY_PIN, GPIO.OUT)

def read_state():
    if not os.path.exists(STATE_FILE):
        return "locked"  # Default state
    with open(STATE_FILE, "r") as f:
        return f.read().strip()

def write_state(state):
    with open(STATE_FILE, "w") as f:
        f.write(state)

def switch_solenoid():
    current_state = read_state()

    if current_state == "locked":
        # Unlock
        GPIO.output(RELAY_PIN, GPIO.LOW)  # Active LOW → unlock
        write_state("unlocked")
        print("🔓 Solenoid UNLOCKED")
    else:
        # Lock
        GPIO.output(RELAY_PIN, GPIO.HIGH)  # Relay OFF → lock
        write_state("locked")
        print("🔒 Solenoid LOCKED")

if __name__ == "__main__":
    try:
        switch_solenoid()
    finally:
        GPIO.cleanup()
import RPi.GPIO as GPIO
import os

RELAY_PIN = 17  # GPIO pin connected to relay IN
STATE_FILE = "lock_state.txt"

# Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(RELAY_PIN, GPIO.OUT)

def read_state():
    if not os.path.exists(STATE_FILE):
        return "locked"  # Default state
    with open(STATE_FILE, "r") as f:
        return f.read().strip()

def write_state(state):
    with open(STATE_FILE, "w") as f:
        f.write(state)

def switch_solenoid():
    current_state = read_state()

    if current_state == "locked":
        # Unlock
        GPIO.output(RELAY_PIN, GPIO.LOW)  # Active LOW → unlock
        write_state("unlocked")
        print("🔓 Solenoid UNLOCKED")
    else:
        # Lock
        GPIO.output(RELAY_PIN, GPIO.HIGH)  # Relay OFF → lock
        write_state("locked")
        print("🔒 Solenoid LOCKED")

if __name__ == "__main__":
    try:
        switch_solenoid()
    finally:
        GPIO.cleanup()
