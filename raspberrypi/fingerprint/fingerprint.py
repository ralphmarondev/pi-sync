import serial
import time

# Open serial connection to R307 (update port accordingly)
ser = serial.Serial("/dev/serial0", baudrate=57600, timeout=1)

# Function to send data to fingerprint sensor
def send_command(command):
    ser.write(command)
    time.sleep(0.1)

# Function to wait for fingerprint capture and process it
def enroll_fingerprint():
    # Command to start capturing the fingerprint
    print("Place your finger on the sensor for enrollment...")
    send_command(b'\xEF\x01\xFF\xFF\xFF\xFF\xFF\xFF')  # Example start capture command
    time.sleep(2)

    response = ser.read(9)  # Read the response from the sensor
    if response:
        print("Capture successful! Now, save the fingerprint.")
    else:
        print("Failed to capture the fingerprint. Please try again.")
        return False
    
    # Command to process and store the fingerprint (usually sent as part of the capture process)
    print("Processing and saving fingerprint...")
    send_command(b'\xEF\x01\xFF\xFF\xFF\xFF\xFF\xFF')  # Example save command
    time.sleep(1)
    
    # Simulate saving the fingerprint into the sensor's memory
    response = ser.read(9)
    if response:
        print("Fingerprint saved successfully.")
        return True
    else:
        print("Failed to save the fingerprint. Please try again.")
        return False

# Main code to enroll the fingerprint
print("Initializing fingerprint sensor...")
ser.flushInput()

while True:
    enroll_fingerprint()
    print("Enrollment complete.")
    time.sleep(5)  # Wait before allowing another enrollment

