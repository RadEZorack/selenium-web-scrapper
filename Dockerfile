# Use a Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy application files
COPY app/ /app

# Install Python dependencies
RUN pip install -r /app/requirements.txt

# Run the script
CMD ["python", "/app/main.py"]
