# Base image
FROM python:3.11-slim

# Working directory 
WORKDIR /app

# Install dependencies
RUN pip install prometheus_client

# Copy app
COPY app.py .

# Expose port 
EXPOSE 8080

# Run the server 
CMD ["python3", "app.py"]

