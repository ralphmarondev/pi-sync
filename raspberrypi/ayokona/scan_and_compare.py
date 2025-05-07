import tkinter as tk
from tkinter import messagebox
import requests
import base64
from pyfingerprint.pyfingerprint import PyFingerprint


def fix_base64_padding(b64_string):
    return b64_string + '=' * (-len(b64_string) % 4)


def capture_and_compare():
    try:
        f = PyFingerprint('/dev/ttyUSB0', 57600)
        if not f.verifyPassword():
            raise ValueError('Incorrect fingerprint sensor password!')

        # Clear fingerprint memory (just to avoid confusion with internal storage)
        f.clearDatabase()

        messagebox.showinfo("Fingerprint", "Place your finger on the sensor...")

        while not f.readImage():
            pass

        f.convertImage(0x01)  # Scanned fingerprint in buffer 1

        scanned_chars = f.downloadCharacteristics(0x01)

        # Fetch all fingerprints from API
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
                continue

            try:
                fixed_b64 = fix_base64_padding(b64_template)
                decoded_bytes = base64.b64decode(fixed_b64)
                stored_chars = list(decoded_bytes)

                f.uploadCharacteristics(0x02, stored_chars)  # Load into buffer 2
                score = f.compareCharacteristics()  # Compare buffer 1 and 2

                if score > 50:
                    messagebox.showinfo("Match Found", f"Fingerprint matched: {name}\nScore: {score}")
                    matched = True
                    break

            except Exception as e:
                print(f"[Skipped] {name}: invalid template or error: {e}")
                continue

        if not matched:
            messagebox.showinfo("Not Recognized", "Fingerprint not recognized.")

    except Exception as e:
        print(f"Error: {e}")


# GUI
root = tk.Tk()
root.title("Fingerprint Match")

check_button = tk.Button(root, text="Scan and Match", command=capture_and_compare)
check_button.pack(padx=20, pady=20)

root.mainloop()
