# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the file with the requirements to the container
COPY requirements.txt .

# Install the Python dependencies
# Using --no-cache-dir to keep the image small
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the container
COPY . .

# Expose the port the app runs on
EXPOSE 5000

# Define environment variable for Flask
ENV FLASK_APP=main.py
ENV FLASK_RUN_HOST=0.0.0.0

# Run the application
CMD ["flask", "run"]
