import tensorflow as tf
import numpy as np
from PIL import Image

# Load the saved model
model = tf.keras.models.load_model('mnist_model.h5')

# Load and preprocess the image
image_path = '9.png'
image = Image.open(image_path).convert('L').resize((28, 28))
image_array = np.array(image).reshape(1, 28, 28, 1) / 255.0

# Perform inference
prediction = model.predict(image_array)
predicted_class = np.argmax(prediction)

print(f"Predicted Digit: {predicted_class}")
