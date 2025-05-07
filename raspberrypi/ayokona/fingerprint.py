import tkinter as tk
import requests
import base64
from pyfingerprint.pyfingerprint import PyFingerprint
from lcd_utils import print_bottom  # 👈 Import LCD helper

def fix_base64_padding(b64_string):
    return b64_string + '=' * (-len(b64_string) % 4)

def capture_and_compare():
    try:
        f = PyFingerprint('/dev/ttyUSB0', 57600)
        if not f.verifyPassword():
            raise ValueError('Incorrect fingerprint sensor password!')

        f.clearDatabase()
        print_bottom("Place your finger")

        while not f.readImage():
            pass

        print_bottom("Scanning...")
        f.convertImage(0x01)

        scanned_chars = f.downloadCharacteristics(0x01)

        # Fetch templates from API
        api_url = "http://192.168.1.98:8000/api/fingerprint/"
        response = requests.get(api_url)
        if response.status_code != 200:
            raise Exception("API fetch error")

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

                f.uploadCharacteristics(0x02, stored_chars)
                score = f.compareCharacteristics()

                if score > 50:
                    print_bottom(f"Matched: {name[:12]}")
                    matched = True
                    break

            except Exception as e:
                print(f"[Skipped] {name}: {e}")
                continue

        if not matched:
            print_bottom("Not recognized")

    except Exception as e:
        print(f"Error: {e}")
        print_bottom("Error occurred")

# GUI
root = tk.Tk()
root.title("Fingerprint Match")

check_button = tk.Button(root, text="Scan and Match", command=capture_and_compare)
check_button.pack(padx=20, pady=20)

root.mainloop()
