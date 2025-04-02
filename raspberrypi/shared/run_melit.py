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
    """Preprocess image: read, resize, and extract features."""
    image = cv2.imread(image_path)
    
    if image is None:
        print(f"Error: Unable to read the image at {image_path}. Please check the file path.")
        return None
    
    # Debugging: Check image shape before processing
    print(f"Original Image Shape: {image.shape}")
    
    # Convert the image to RGB (because OpenCV loads in BGR)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Resize image to match the model's expected input shape
    input_shape = input_details[0]['shape']
    print(f"Model Input Shape: {input_shape}")  # Debugging: check model input shape
    
    try:
        image = cv2.resize(image, (input_shape[2], input_shape[1]))  # (height, width)
    except Exception as e:
        print(f"Error resizing image: {e}")
        return None
    
    # Debugging: Check the shape after resizing
    print(f"Resized Image Shape: {image.shape}")
    
    # Normalize image pixel values to [0, 1]
    image = np.array(image, dtype=np.float32) / 255.0
    
    # Extract image features: For example, mean RGB values
    mean_rgb = np.mean(image, axis=(0, 1))  # Mean RGB values across height and width
    
    # Debugging: Check extracted features
    print(f"Extracted Mean RGB Features: {mean_rgb}")
    
    # Make sure the features are the expected shape (10 features)
    if len(mean_rgb) == 3:  # RGB has 3 channels, you may need to add more features here
        features = np.concatenate([mean_rgb, np.zeros(7)])  # Pad to make it 10 features
    else:
        features = mean_rgb
    
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
