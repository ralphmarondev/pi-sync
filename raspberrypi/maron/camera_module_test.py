import libcamera
import time
from picamera2 import Picamera2

# Initialize camera
picam2 = Picamera2()
picam2.configure(picam2.create_still_configuration())

# Start camera preview (optional)
picam2.start()
time.sleep(2)  # Allow time for auto-adjustments

# Capture image
picam2.capture_file("test.jpg")

print("Image saved as test.jpg")
