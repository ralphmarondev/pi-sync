import serial
import time
import hashlib

# Open serial connection to R307 (update port accordingly)
ser = serial.Serial("/dev/serial0", baudrate=57600, timeout=1)

# Function to send data to fingerprint sensor
def send_command(command):
    ser.write(command)
    time.sleep(0.1)

# Function to get the fingerprint ID
def get_fingerprint_id():
    # Command to capture the fingerprint
    send_command(b'\xEF\x01\xFF\xFF\xFF\xFF\xFF\xFF')  # Example of command to start capture
    time.sleep(2)  # Give time for sensor to process
    response = ser.read(9)  # Read 9 bytes of response from sensor
    
    if response:
        print("Response:", response)
        return response  # Returning the response (you would want to process this for ID)
    else:
        print("No fingerprint found")
        return None

# Function to compare two fingerprints
def compare_fingerprints(fingerprint1, fingerprint2):
    # Simple comparison by hashing the data to compare
    hash1 = hashlib.sha256(fingerprint1).hexdigest()
    hash2 = hashlib.sha256(fingerprint2).hexdigest()
    return hash1 == hash2

# Initialize the fingerprint sensor
print("Initializing fingerprint sensor...")
ser.flushInput()

# Variable to store the first fingerprint (None initially)
stored_fingerprint = None

# Test loop
while True:
    print("Place your finger on the sensor...")
    
    # Get the fingerprint data
    current_fingerprint = get_fingerprint_id()
    
    if current_fingerprint:
        if stored_fingerprint is None:
            # This is the first fingerprint (enroll it)
            stored_fingerprint = current_fingerprint
            print("Fingerprint enrolled!")
        else:
            # Compare current fingerprint with the stored one
            if compare_fingerprints(stored_fingerprint, current_fingerprint):
                print("Fingerprint matched!")
            else:
                print("Fingerprint did not match!")
    else:
        print("No match found.")
    
    time.sleep(5)  # Wait before next scan
