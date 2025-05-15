import tkinter as tk
from tkinter import messagebox
import requests
import base64
import time
from pyfingerprint.pyfingerprint import PyFingerprint
import threading
from lcd_utils import write_bottom

API_URL = 'http://192.168.1.98:8000/api'

def fetch_users_with_templates():
    try:
        response = requests.get(f'{API_URL}/users/')
        if response.status_code == 200:
            users = response.json().get('users', [])
            templates = []

            for user in users:
                username = user.get("username")
                template_name = user.get("fingerprint_template")

                if template_name:
                    template_data = fetch_template_detail(template_name)
                    if template_data:
                        templates.append({
                            "username": username,
                            "template": template_data
                        })
            return templates
        else:
            print("Failed to fetch users.")
            return []
    except Exception as e:
        print(f"API error: {e}")
        return []

def fetch_template_detail(template_name):
    try:
        response = requests.get(f'{API_URL}/fingerprint/details/{template_name}/')
        if response.status_code == 200:
            return response.json().get('template')
        else:
            print(f"Failed to fetch template for {template_name}")
            return None
    except Exception as e:
        print(f"API error while fetching template {template_name}: {e}")
        return None

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

def open_door_api(username):
    try:
        data = {
            'username': username,
            'description': 'opened via fingerprint'
        }
        response = requests.post(f'{API_URL}/door/open/1/', json=data)
        if response.status_code == 200:
            print("Door opened successfully.")
        else:
            print(f"Failed to open door. Status: {response.status_code}")
    except Exception as e:
        print(f"API door open error: {e}")

def match_fingerprint(f, templates):
    try:
        print("Waiting for finger...")
        while not f.readImage():
            time.sleep(0.1)

        f.convertImage(0x01)
        scanned_char = f.downloadCharacteristics(0x01)

        for item in templates:
            username = item["username"]
            template_b64 = item["template"]

            try:
                stored_char_bytes = base64.b64decode(template_b64 + '===')
                stored_char = list(stored_char_bytes)
                f.uploadCharacteristics(0x02, stored_char)
                score = f.compareCharacteristics()
                if score >= 50:
                    return username
            except Exception as e:
                print(f"Failed to compare with {username}: {e}")
        return None

    except Exception as e:
        print(f"Scan error: {e}")
        return None

def fingerprint_loop():
    f = initialize_sensor()
    if not f:
        return

    templates = fetch_users_with_templates()

    while True:
        matched_username = match_fingerprint(f, templates)
        if matched_username:
            print(f"Fingerprint matched: {matched_username}")
            write_bottom('Welcome home!')
            open_door_api(matched_username)
            time.sleep(3)
        else:
            print("Fingerprint not recognized")
            write_bottom('Not recognized')
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
