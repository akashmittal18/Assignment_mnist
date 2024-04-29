# Use the official lightweight Python image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install Flask and other dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

# Expose port 5000 to allow communication to the Flask app
EXPOSE 5000

# Define environment variable
ENV FLASK_APP flask_app.py

# Command to run the Flask app
CMD ["flask", "run", "--host=0.0.0.0"]
