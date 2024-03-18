# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster

# Set the working directory in the container
WORKDIR /app

# Create a directory called temp within the /app directory with appropriate permissions
RUN mkdir -p temp && chown 1000:1000 temp

# Copy the current directory contents into the container at /app
COPY . /app

# Apt install
RUN apt-get update && apt-get install -y libmagic1

# Upgrade pip
RUN pip install --upgrade pip

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run Gunicorn to start the Flask application
CMD ["gunicorn", "-c", "gunicorn_config.py", "app:app"]
