# DOCKERFILE

#Base Image
FROM python:3.11-slim

# Install system tools 
RUN apt-get update && apt-get install -y procps && rm -rf /var/lib/apt/lists/*

#Working Directory inside the container
WORKDIR /app

#Copy script to container
COPY system_info.py .

#Run the scripts when container start
CMD ["python3", "system_info.py"] 
 

