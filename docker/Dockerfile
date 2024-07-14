# Use an official Python runtime as the base image
FROM python:3.8


# Install Git
RUN apt-get update && apt-get install -y git gcc


# Set the working directory in the container
WORKDIR /app


# Copy the requirements file into the container
COPY ../requirements.txt ../


# Install the Python dependencies
RUN pip3 install --no-cache-dir -r ../requirements.txt


# Copy the rest of the application code into the container
COPY ../ ../


# Set the command to run the application
CMD [ "python", "run.py" ]