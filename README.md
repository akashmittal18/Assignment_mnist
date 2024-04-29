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
