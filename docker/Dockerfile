# Base Image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose ports
EXPOSE 8000 8001 8002 8003 8004 8005 8006

# Set the entrypoint
ENTRYPOINT ["bash", "./docker/entrypoint.sh"]
