import serial
import time

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
        # Process the response here (compare with known fingerprints)
        return True
    else:
        print("No fingerprint found")
        return False

# Initialize the fingerprint sensor
print("Initializing fingerprint sensor...")
ser.flushInput()

# Test loop
while True:
    print("Place your finger on the sensor...")
    if get_fingerprint_id():
        print("Fingerprint matched!")
    else:
        print("No match found.")
    time.sleep(5)  # Wait before next scan
