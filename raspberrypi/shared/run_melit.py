import tensorflow as tf
import numpy as np
import cv2

# Load the TFLite ..
interpreter = tf.lite.Interpreter(model_path="marylitte.tflite")
interpreter.allocate_tensors()

# Get input and output tensors
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Debugging: Check input and output tensor details
print("Input Details:", input_details)
print("Output Details:", output_details)

def preprocess_image(image_path):
    """Preprocess image: read, extract features."""
    image = cv2.imread(image_path)
    
    if image is None:
        print(f"Error: Unable to read the image at {image_path}. Please check the file path.")
        return None
    
    # Debugging: Check image shape before processing
    print(f"Original Image Shape: {image.shape}")
    
    # Convert the image to RGB (because OpenCV loads in BGR)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Resize image for consistency
    max_size = 224  # Example size for consistency in feature extraction
    scale = max_size / max(image.shape[:2])
    new_size = tuple((np.array(image.shape[:2]) * scale).astype(int))
    image = cv2.resize(image, (new_size[1], new_size[0]))

    # Debugging: Check the resized image shape
    print(f"Resized Image Shape: {image.shape}")

    # Normalize the image (scale to [0, 1])
    image = np.array(image, dtype=np.float32) / 255.0
    
    # Extract 10 features (example: mean RGB and other statistics)
    mean_rgb = np.mean(image, axis=(0, 1))  # Mean RGB values across height and width
    std_rgb = np.std(image, axis=(0, 1))    # Standard deviation for RGB
    
    # Example of other statistics: (you can change this as needed)
    max_rgb = np.max(image, axis=(0, 1))
    
    # Combine all features into a single vector of length 10
    # We will now just use mean RGB, std RGB, and max RGB (9 features)
    features = np.concatenate([mean_rgb, std_rgb, max_rgb])
    
    # Add an additional feature (optional, e.g., max value across the entire image)
    # Here we add the maximum pixel value as the 10th feature
    max_pixel = np.max(image)
    
    features = np.concatenate([features, [max_pixel]])  # Ensure the vector has exactly 10 features
    
    # Ensure the features vector has exactly 10 elements (padded or adjusted as needed)
    features = np.expand_dims(features, axis=0)  # Add batch dimension
    
    return features

def classify_cacao(image_path):
    """Classify cacao bean based on extracted features."""
    features = preprocess_image(image_path)
    if features is None:
        print("Error: Image preprocessing failed.")
        return
    
    # Set the features to the input tensor of the model
    interpreter.set_tensor(input_details[0]['index'], features)
    interpreter.invoke()
    
    # Get the output from the model
    output_data = interpreter.get_tensor(output_details[0]['index'])
    
    # Debugging: Check the raw output data
    print(f"Output Data: {output_data}")
    
    # Get the predicted class
    predicted_class = np.argmax(output_data)
    
    # Define class names
    class_names = ["Criollo", "Forastero", "Trinitario"]
    
    if predicted_class < len(class_names):
        result = class_names[predicted_class]
    else:
        result = "Unknown"
    
    print(f"Predicted class: {result}")
    return result

if __name__ == "__main__":
    image_path = "test_cacao_thingy.jpg"  # Change this to your test image
    classify_cacao(image_path)
