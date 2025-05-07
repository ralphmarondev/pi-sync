import tkinter as tk
from tkinter import messagebox
import requests
import base64
from pyfingerprint.pyfingerprint import PyFingerprint


def fix_base64_padding(b64_string):
    """Fix base64 padding errors by adjusting to a multiple of 4"""
    return b64_string + '=' * (-len(b64_string) % 4)


def capture_and_compare():
    try:
        # Initialize fingerprint sensor
        f = PyFingerprint('/dev/ttyUSB0', 57600)
        if not f.verifyPassword():
            raise ValueError('Incorrect fingerprint sensor password!')

        # Clear fingerprint memory
        f.clearDatabase()

        messagebox.showinfo("Fingerprint", "Place your finger on the sensor...")

        # Wait for finger
        while not f.readImage():
            pass

        f.convertImage(0x01)

        # Get scanned fingerprint characteristics
        scanned_chars = f.downloadCharacteristics(0x01)

        # Fetch stored templates from API
        api_url = "http://192.168.1.98:8000/api/fingerprint/"
        response = requests.get(api_url)
        if response.status_code != 200:
            raise Exception("Failed to fetch fingerprints from API")

        fingerprints = response.json()
        matched = False

        for fp in fingerprints:
            name = fp.get("name")
            b64_template = fp.get("template")

            if not name or not b64_template:
                continue  # skip incomplete data

            try:
                fixed_b64 = fix_base64_padding(b64_template)
                decoded_bytes = base64.b64decode(fixed_b64)
                stored_chars = list(decoded_bytes)
            except Exception as e:
                print(f"[Skipped] {name} due to invalid Base64: {e}")
                continue

            score = f.compareCharacteristics(scanned_chars, stored_chars)
            if score > 50:
                messagebox.showinfo("Match Found", f"Fingerprint matched: {name} (Score: {score})")
                matched = True
                break

        if not matched:
            messagebox.showinfo("Not Recognized", "Fingerprint not recognized.")

    except Exception as e:
        print(f"Error: {e}")


# GUI setup
root = tk.Tk()
root.title("Fingerprint Matching")

check_button = tk.Button(root, text="Scan and Match", command=capture_and_compare)
check_button.pack(padx=20, pady=20)

root.mainloop()
