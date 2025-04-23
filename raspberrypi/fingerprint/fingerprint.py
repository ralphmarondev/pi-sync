import serial

ser = serial.Serial('/dev/serial0', 57600, timeout=1)
ser.write(b'\xEF\x01\xFF\xFF\xFF\xFF\x01\x00\x03\x01\x00\x05')  # Handshake packet
response = ser.read(12)
print(response)
