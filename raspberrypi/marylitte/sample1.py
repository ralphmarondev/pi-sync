import cv2
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import customtkinter as ctk
from PIL import Image, ImageTk
import os  # For file and folder operations

# Dataset thingy, the more the better
data = [
    # Crollio (white beans)
    [30, 50, 70, 'Crollio'], [32, 52, 72, 'Crollio'], [28, 48, 68, 'Crollio'], [35, 55, 75, 'Crollio'],
    [33, 53, 73, 'Crollio'], [29, 49, 69, 'Crollio'], [31, 51, 71, 'Crollio'], [34, 54, 74, 'Crollio'],
    [27, 47, 67, 'Crollio'], [36, 56, 76, 'Crollio'], [30, 50, 70, 'Crollio'], [32, 52, 72, 'Crollio'],
    [28, 48, 68, 'Crollio'], [35, 55, 75, 'Crollio'], [33, 53, 73, 'Crollio'], [29, 49, 69, 'Crollio'],
    [31, 51, 71, 'Crollio'], [34, 54, 74, 'Crollio'], [27, 47, 67, 'Crollio'], [36, 56, 76, 'Crollio'],

    # Forastero (dark-purple beans)
    [120, 80, 90, 'Forastero'], [122, 82, 92, 'Forastero'], [118, 78, 88, 'Forastero'], [125, 85, 95, 'Forastero'],
    [123, 83, 93, 'Forastero'], [119, 79, 89, 'Forastero'], [121, 81, 91, 'Forastero'], [124, 84, 94, 'Forastero'],
    [117, 77, 87, 'Forastero'], [126, 86, 96, 'Forastero'], [120, 80, 90, 'Forastero'], [122, 82, 92, 'Forastero'],
    [118, 78, 88, 'Forastero'], [125, 85, 95, 'Forastero'], [123, 83, 93, 'Forastero'], [119, 79, 89, 'Forastero'],
    [121, 81, 91, 'Forastero'], [124, 84, 94, 'Forastero'], [117, 77, 87, 'Forastero'], [126, 86, 96, 'Forastero'],

    # Trinotario (combination of Crollio and Forastero)
    [60, 100, 110, 'Trinotario'], [62, 102, 112, 'Trinotario'], [58, 98, 108, 'Trinotario'], [65, 105, 115, 'Trinotario'],
    [63, 103, 113, 'Trinotario'], [59, 99, 109, 'Trinotario'], [61, 101, 111, 'Trinotario'], [64, 104, 114, 'Trinotario'],
    [57, 97, 107, 'Trinotario'], [66, 106, 116, 'Trinotario'], [60, 100, 110, 'Trinotario'], [62, 102, 112, 'Trinotario'],
    [58, 98, 108, 'Trinotario'], [65, 105, 115, 'Trinotario'], [63, 103, 113, 'Trinotario'], [59, 99, 109, 'Trinotario'],
    [61, 101, 111, 'Trinotario'], [64, 104, 114, 'Trinotario'], [57, 97, 107, 'Trinotario'], [66, 106, 116, 'Trinotario'],

    # Additional random samples for variety
    [40, 60, 80, 'Crollio'], [130, 90, 100, 'Forastero'], [70, 110, 120, 'Trinotario'], [45, 65, 85, 'Crollio'],
    [135, 95, 105, 'Forastero'], [75, 115, 125, 'Trinotario'], [50, 70, 90, 'Crollio'], [140, 100, 110, 'Forastero'],
    [80, 120, 130, 'Trinotario'], [55, 75, 95, 'Crollio'], [145, 105, 115, 'Forastero'], [85, 125, 135, 'Trinotario'],
    [60, 80, 100, 'Crollio'], [150, 110, 120, 'Forastero'], [90, 130, 140, 'Trinotario'], [65, 85, 105, 'Crollio'],
    [155, 115, 125, 'Forastero'], [95, 135, 145, 'Trinotario'], [70, 90, 110, 'Crollio'], [160, 120, 130, 'Forastero']
]

X = [d[:3] for d in data]  # Features (HSV)
y = [d[3] for d in data]  # Labels

# Train a classifier
clf = RandomForestClassifier()
clf.fit(X, y)

# Create a dataset folder if it doesn't exist
dataset_folder = "dataset"
if not os.path.exists(dataset_folder):
    os.makedirs(dataset_folder)

# Function to get the next available filename
def get_next_filename(folder):
    files = os.listdir(folder)
    numbers = [int(f.split('.')[0]) for f in files if f.endswith('.jpg') and f.split('.')[0].isdigit()]
    return f"{max(numbers) + 1 if numbers else 0}.jpg"

# Function to capture an image, classify the bean, and save the image
def capture_and_classify():
    # Open webcam
    cap = cv2.VideoCapture(1)
    ret, frame = cap.read()
    cap.release()

    if ret:
        # Convert to HSV
        hsv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        average_color = np.mean(hsv_image.reshape(-1, 3), axis=0)

        # Predict the bean type
        prediction = clf.predict([average_color])
        result_label.configure(text=f'The bean is classified as: {prediction[0]}')

        # Save the captured image
        filename = get_next_filename(dataset_folder)
        filepath = os.path.join(dataset_folder, filename)
        cv2.imwrite(filepath, frame)
        print(f"Image saved as {filepath}")

        # Display the captured image in the GUI
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        img = img.resize((300, 300))  # Resize for display
        img_tk = ImageTk.PhotoImage(img)
        image_label.configure(image=img_tk)
        image_label.image = img_tk
    else:
        result_label.configure(text="Failed to capture image.")

# Create the GUI
app = ctk.CTk()
app.title("Bean Classifier")
app.geometry("400x500")

# Add a label to display the captured image
image_label = ctk.CTkLabel(app, text="")
image_label.pack(pady=10)

# Add a button to capture and classify the bean
capture_button = ctk.CTkButton(app, text="Capture and Classify", command=capture_and_classify)
capture_button.pack(pady=10)

# Add a label to display the result
result_label = ctk.CTkLabel(app, text="")
result_label.pack(pady=10)

# Run the GUI
app.mainloop()
