import tkinter as tk
from tkinter import messagebox
import requests
import base64
import time
from pyfingerprint.pyfingerprint import PyFingerprint
import threading

API_URL = 'http://192.168.1.98:8000/api'

def fetch_templates_from_api():
    try:
        response = requests.get(f'{API_URL}/fingerprint/')
        if response.status_code == 200:
            return response.json()
        else:
            print("Failed to fetch templates.")
            return []
    except Exception as e:
        print(f"API error: {e}")
        return []

def initialize_sensor():
    try:
        f = PyFingerprint('/dev/ttyUSB0', 57600)
        if not f.verifyPassword():
            raise ValueError('Incorrect fingerprint sensor password!')
        f.clearDatabase()  # Clear memory before use
        return f
    except Exception as e:
        print(f"Sensor initialization failed: {e}")
        return None

def open_door_api(name):
    try:
        data = {
            'username': name,
            'description': 'opened via fingerprint'
        }
        response = requests.post(f'{API_URL}/door/open/1/', json=data)
        if response.status_code == 200:
            print("Door opened successfully.")
        else:
            print(f"Failed to open door. Status: {response.status_code}")
    except Exception as e:
        print(f"API door open error: {e}")

def match_fingerprint(f, api_templates):
    try:
        print("Waiting for finger...")
        while not f.readImage():
            time.sleep(0.1)

        f.convertImage(0x01)
        scanned_char = f.downloadCharacteristics(0x01)

        for template in api_templates:
            name = template.get("name")
            template_b64 = template.get("template")
            try:
                stored_char_bytes = base64.b64decode(template_b64 + '===')
                stored_char = list(stored_char_bytes)
                f.uploadCharacteristics(0x02, stored_char)
                score = f.compareCharacteristics()
                if score >= 50:
                    return name
            except Exception as e:
                print(f"Failed to compare with {name}: {e}")
        return None

    except Exception as e:
        print(f"Scan error: {e}")
        return None

def fingerprint_loop():
    f = initialize_sensor()
    if not f:
        return

    api_templates = fetch_templates_from_api()

    while True:
        matched_name = match_fingerprint(f, api_templates)
        if matched_name:
            # messagebox.showinfo("Success", f"Fingerprint matched: {matched_name}")
            print(f"Fingerprint matched: {matched_name}")
            open_door_api(matched_name)
            time.sleep(3)
        else:
            print("Fingerprint not recognized")
        time.sleep(1)

def start_fingerprint_thread():
    thread = threading.Thread(target=fingerprint_loop, daemon=True)
    thread.start()

# GUI Setup
root = tk.Tk()
root.title("Smart Door System")

# Display Info
tk.Label(root, text="Thesis Computer Engineering", font=("Helvetica", 16, "bold")).pack(pady=5)
tk.Label(root, text="Batch 2024-2025", font=("Helvetica", 12)).pack(pady=2)
tk.Label(root, text="Members:", font=("Helvetica", 12, "underline")).pack(pady=5)
tk.Label(root, text="Ralph Maron A. Eda", font=("Helvetica", 11)).pack()
tk.Label(root, text="Jack Cabigayan", font=("Helvetica", 11)).pack()
tk.Label(root, text="Triesha Mae Olunan", font=("Helvetica", 11)).pack()
tk.Label(root, text="Jezlyn Cabbab", font=("Helvetica", 11)).pack()

# Start fingerprint detection in background
start_fingerprint_thread()

# Launch GUI
root.mainloop()
