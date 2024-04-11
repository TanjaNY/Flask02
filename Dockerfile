# Use an official Python runtime as a parent image
FROM python:3.9-slim AS base

# Set environment variables

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

# Corrected CMD instruction
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0", "--port=5004"]

