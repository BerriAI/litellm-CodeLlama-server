# Use a recent version of Python as the base image
FROM python:3.8-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the requirements.txt file to the image
COPY requirements.txt .

# Install the required packages

# Install the required Python packages using pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files to the image
COPY . .

# Expose port 4000 for the Flask app to listen on
EXPOSE 4000

# Run the main.py file when the container is started
CMD ["python", "main.py"]