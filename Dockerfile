# Use the official Python image as base
FROM python:3.11-slim

# Set the working directory in the container to /app
WORKDIR /app

# Copy only the necessary directories into the container
COPY cli /app/cli
COPY app /app/app
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set the environment variable to ensure Python outputs are sent straight to terminal without being buffered
ENV PYTHONUNBUFFERED 1

# Command to run when the container starts, this will run the cli.main as the entry point
CMD ["python3", "-m", "cli.main"]
