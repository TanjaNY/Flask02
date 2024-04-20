# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container to /python-docker
WORKDIR /python-docker

# Copy the dependencies file
COPY requirements.txt requirements.txt

# Install dependencies
RUN pip3 install -r requirements.txt

# Copy the application code
COPY . .

# Set up SQLite database
RUN apt-get update && apt-get install -y sqlite3
RUN mkdir -p /python-docker && sqlite3 /python-docker/app.db

# Corrected CMD instruction
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0", "--port=5005"]
