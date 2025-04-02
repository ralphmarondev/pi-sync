import tkinter as tk
from tkinter import Label, Button

import cv2
import numpy as np
# Initialize global variables
recognizer = cv2.face.LBPHFaceRecognizer_create()
reference_image_path = "reference3.jpg"
result_text = ""

def train_reference_image():
	reference_gray = cv2.imread(reference_image_path, cv2.IMREAD_GRAYSCALE)
	if reference_gray is None:
		print("Reference image not found!")
		return False

	# Convert labels to a NumPy array
	labels = np.array([0])  # Label for the reference image

	# Train the recognizer
	recognizer.train([reference_gray], labels)
	return True

# Capture an image using the webcam and compare it with the reference
def capture_and_compare():
	global result_text
	# Open the webcam
	cap = cv2.VideoCapture(0)

	# Capture a single frame
	ret, frame = cap.read()
	cap.release()  # Release the webcam

	if not ret:
		result_text = "Failed to capture image!"
		update_label()
		return

	# Convert to grayscale
	captured_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	# Save the captured image (optional, for debugging)
	cv2.imwrite("captured.jpg", captured_gray)

	# Predict the captured image
	label, confidence = recognizer.predict(captured_gray)
	if confidence < 50:  # Confidence threshold
		result_text = f"Face matches! (Confidence: {confidence:.2f})"
	else:
		result_text = f"Face does not match. (Confidence: {confidence:.2f})"

	# Update the result on the screen
	update_label()

# Update the result label on the Tkinter window
def update_label():
	result_label.config(text=result_text)

# Initialize the Tkinter window
def main():
	global result_label

	# Create the main window
	window = tk.Tk()
	window.title("Face Recognition App")
	window.geometry("400x300")

	# Add a label for instructions
	instruction_label = Label(window, text="Click the button to capture an image and compare.")
	instruction_label.pack(pady=20)

	# Add a button to capture and compare
	capture_button = Button(window, text="Capture and Compare", command=capture_and_compare)
	capture_button.pack(pady=10)

	# Add a label to show the result
	result_label = Label(window, text="", fg="blue")
	result_label.pack(pady=20)

	# Train the reference image
	if not train_reference_image():
		result_label.config(text="Error: Reference image not found!")

	# Start the Tkinter loop
	window.mainloop()

if __name__ == "__main__":
	main()
