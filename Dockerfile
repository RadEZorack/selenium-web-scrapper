# Use a Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy application files
COPY app/ /app

# Install Python dependencies
RUN pip install -r /app/requirements.txt

# Add wait-for-it script to the container
COPY wait-for-it.sh /wait-for-it.sh
RUN chmod +x /wait-for-it.sh

# Run the script
CMD ["/wait-for-it.sh", "selenium:4444", "--", "python", "/app/main.py"]
