import tensorflow as tf

# Sample model (you should replace this with your actual trained model)
def create_model():
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(16, activation='relu', input_shape=(10,)),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model

# Create and save the model
model = create_model()
model.save("marylitte.h5")  # Save in HDF5 format

# Load and convert the model to TensorFlow Lite format
model = tf.keras.models.load_model("marylitte.h5")
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

# Save the TFLite model
with open("marylitte.tflite", "wb") as f:
    f.write(tflite_model)

print("Conversion successful: marylitte.tflite created!")
