import time
from tkinter import *
from tkinter import messagebox
from pyfingerprint.pyfingerprint import PyFingerprint

# Attempt to initialize the fingerprint sensor
def init_sensor():
    try:
        sensor = PyFingerprint('/dev/serial0', 57600, 0xFFFFFFFF, 0x00000000)

        if not sensor.verifyPassword():
            raise ValueError('Invalid fingerprint sensor password.')
        
        return sensor

    except Exception as e:
        messagebox.showerror("Initialization Failed", f"Could not initialize sensor.\n\n{e}")
        return None

f = init_sensor()
if f is None:
    exit(1)

# GUI functions
def enroll():
    try:
        messagebox.showinfo("Enroll", "Place finger on sensor...")
        while not f.readImage():
            pass

        f.convertImage(0x01)

        result = f.searchTemplate()
        positionNumber = result[0]

        if positionNumber >= 0:
            messagebox.showinfo("Enroll", "Fingerprint already exists.")
            return

        messagebox.showinfo("Enroll", "Remove finger...")
        time.sleep(2)

        messagebox.showinfo("Enroll", "Place the same finger again...")
        while not f.readImage():
            pass

        f.convertImage(0x02)

        if f.compareCharacteristics() == 0:
            raise Exception('Fingerprints do not match.')

        f.createTemplate()
        positionNumber = f.storeTemplate(0)
        messagebox.showinfo("Success", f"Fingerprint enrolled at position {positionNumber}.")

    except Exception as e:
        messagebox.showerror("Error", str(e))

def search():
    try:
        messagebox.showinfo("Search", "Place finger on sensor...")
        while not f.readImage():
            pass

        f.convertImage(0x01)

        result = f.searchTemplate()
        positionNumber = result[0]
        accuracyScore = result[1]

        if positionNumber == -1:
            messagebox.showinfo("Result", "No match found.")
        else:
            messagebox.showinfo("Match Found", f"Match found at position {positionNumber}\nAccuracy: {accuracyScore}")

    except Exception as e:
        messagebox.showerror("Error", str(e))

# Build the GUI
app = Tk()
app.title("R307 Fingerprint with GPIO UART")
app.geometry("320x220")
app.resizable(False, False)

Label(app, text="R307 Fingerprint Test", font=("Arial", 14)).pack(pady=15)

Button(app, text="Enroll Fingerprint", command=enroll, width=25).pack(pady=10)
Button(app, text="Search Fingerprint", command=search, width=25).pack(pady=10)

Label(app, text="Make sure UART is enabled!", font=("Arial", 9), fg="gray").pack(pady=10)

app.mainloop()
