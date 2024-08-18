# Use Python runtime as base image
FROM python:3.9-slim

# Set working directory in container
WORKDIR /app

# Copy requirements file to container
COPY requirements.txt .

# Install the project dependencies

RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files to container
COPY . .

# Expose the port the app runs on
EXPOSE 5000

# Command to run application
CMD ["python", "backend/run.py"]