## Assignment_mnist



1. mnist_train.py- Training Script for MNIST model
2. mnist_inference.py- Inference script for testing the model locally
3. flask_app.py- Rest Endpoint script using flask framework
4. Dockerfile- Contains script for docker image creation
5. mnist_model.h5- Saved model file

   Curl Command for inference
```cmd
!curl -X POST -F "image=@"C:\Users\934624\Downloads\9.png"" http://localhost:5000/predict
```
