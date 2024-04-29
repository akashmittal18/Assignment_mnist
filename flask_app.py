from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np
from PIL import Image

app = Flask(__name__)

# Load the saved model
model = tf.keras.models.load_model('mnist_model.h5')

@app.route('/predict', methods=['POST'])
def predict():
    # Get image data from request
    image_data = request.files['image']
    image = Image.open(image_data).convert('L').resize((28, 28))
    image_array = np.array(image).reshape(1, 28, 28, 1) / 255.0

    # Perform inference
    prediction = model.predict(image_array)
    predicted_class = np.argmax(prediction)

    return jsonify({'predicted_digit': int(predicted_class)})

if __name__ == '__main__':
    app.run(host='0.0.0.0')
