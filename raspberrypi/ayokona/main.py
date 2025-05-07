import tkinter as tk
from tkinter import messagebox
import requests
import base64
from pyfingerprint.pyfingerprint import PyFingerprint

def read_and_test_fingerprint():
    try:
        # Initialize sensor
        f = PyFingerprint('/dev/ttyUSB0', 57600)
        if not f.verifyPassword():
            raise ValueError('Incorrect fingerprint sensor password!')

        messagebox.showinfo("Fingerprint", "Place your finger on the sensor...")

        # Wait for a finger to be read
        while not f.readImage():
            pass

        f.convertImage(0x01)

        # Download scanned fingerprint characteristics
        scanned = f.downloadCharacteristics(0x01)

        # Fetch all stored templates
        response = requests.get("http://192.168.1.98:8000/api/fingerprint/")
        if response.status_code != 200:
            raise Exception(f"Failed to fetch templates: {response.status_code}")

        templates = response.json()

        for item in templates:
            name = item.get("name")
            template_b64 = item.get("template")

            if not template_b64:
                continue

            # Decode base64 string to bytes then to list of ints
            decoded = base64.b64decode(template_b64)
            template_chars = list(decoded)

            # Upload downloaded template to char buffer 2
            f.uploadCharacteristics(0x02, template_chars)

            # Compare with current scanned fingerprint in buffer 1
            score = f.compareCharacteristics()

            if score >= 50:  # You can tweak the threshold
                messagebox.showinfo("Match Found", f"Matched with: {name}\nMatch Score: {score}")
                return

        messagebox.showinfo("No Match", "Fingerprint not recognized.")

    except Exception as e:
        messagebox.showerror("Error", f"Matching failed: {str(e)}")

# GUI setup
root = tk.Tk()
root.title("Test Fingerprint Against API")

match_button = tk.Button(root, text="Read & Test Fingerprint", command=read_and_test_fingerprint)
match_button.pack(padx=20, pady=20)

root.mainloop()
