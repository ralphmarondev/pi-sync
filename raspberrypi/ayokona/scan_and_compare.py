import base64
import requests
import tkinter as tk
from tkinter import messagebox
from pyfingerprint.pyfingerprint import PyFingerprint

def match_fingerprint():
    try:
        # Initialize the fingerprint sensor
        f = PyFingerprint('/dev/ttyUSB0', 57600)

        if not f.verifyPassword():
            raise ValueError('Incorrect fingerprint sensor password!')

        messagebox.showinfo("Fingerprint", "Place your finger on the sensor...")

        while not f.readImage():
            pass

        f.convertImage(0x01)

        # Download the scanned fingerprint characteristics
        scanned_characteristics = f.downloadCharacteristics(0x01)
        scanned_bytes = bytearray(scanned_characteristics)

        # Get list of stored fingerprints from the API
        api_url = 'http://192.168.1.98:8000/api/fingerprint/'
        response = requests.get(api_url)

        if response.status_code != 200:
            messagebox.showerror("Error", "Failed to fetch fingerprints from API")
            return

        fingerprints = response.json()

        # Compare with each fingerprint in the list
        for fp in fingerprints:
            stored_template_b64 = fp['template']
            stored_name = fp['name']

            stored_bytes = base64.b64decode(stored_template_b64)
            stored_characteristics = list(stored_bytes)

            score = f.compareCharacteristics(scanned_characteristics, stored_characteristics)

            if score > 50:  # Matching threshold, adjust as needed
                messagebox.showinfo("Match Found", f"Fingerprint matched: {stored_name}\nScore: {score}")
                return

        messagebox.showinfo("No Match", "Fingerprint not recognized.")

    except Exception as e:
        print(f"Error: {str(e)}")

# Create basic GUI for testing
root = tk.Tk()
root.title("Fingerprint Matcher")

match_button = tk.Button(root, text="Scan & Match Fingerprint", command=match_fingerprint)
match_button.pack(padx=20, pady=20)

root.mainloop()
