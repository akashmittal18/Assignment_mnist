## Assignment on MNIST

This repo contains code files for MNIST Problem along with its docker file.


1. mnist_train.py- Training Script for MNIST model
2. mnist_inference.py- Inference script for testing the model locally
3. flask_app.py- Rest Endpoint script using flask framework
4. Dockerfile- Contains script for docker image creation
5. mnist_model.h5- Saved model file

   Curl Command for inference
```cmd
!curl -X POST -F "image=@"C:\Users\934624\Downloads\9.png"" http://localhost:5000/predict
```
Screenshot of the post request done locally using curl
<img width="1130" alt="Screenshot 2024-04-29 at 5 38 43 PM" src="https://github.com/akashmittal18/Assignment_mnist/assets/47140557/84b6107d-4407-42d2-9f79-d548a5aeb35f">


## Flow of Requests:

1. Client Request: The client (such as Postman or cURL) sends a POST request to the Flask web application running inside the Docker container. The request contains an image file representing a handwritten digit.

2. Flask Web Application: The Flask web application receives the POST request. It extracts the image data from the request and preprocesses it to prepare it for inference.

3. Model Inference: The preprocessed image data is passed to the loaded TensorFlow model for inference. The model predicts the digit represented by the image.

4. Response Generation: The predicted digit is sent back as a response from the Flask web application. The response is typically in JSON format, containing the predicted digit.

5. Client Response: The client (Postman or cURL) receives the response from the Flask web application. It can then process the response, display the predicted digit, or perform any further actions required.

This architecture allows for easy deployment and scaling of the inference service. The Docker container encapsulates the Flask application and all its dependencies, making it portable and easy to deploy in various environments. The Flask application provides a simple REST API for performing inference, making it accessible to a wide range of clients.

## Architecture Diagram

<img width="693" alt="Screenshot 2024-04-29 at 9 32 31 PM" src="https://github.com/akashmittal18/Assignment_mnist/assets/47140557/38ffe8c0-e3c8-413f-a98d-d5a4ebe9b9dd">

