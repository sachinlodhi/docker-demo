#!/bin/bash

# Build the image
docker build -t my-flask-app:latest .

# List images to verify
docker images

# Run container in background
docker run -d \
  --name flask-container \
  -p 8080:5000 \
  -e ENV=production \
  my-flask-app:latest

# Check if container is running
docker ps

# View container logs
docker logs flask-container

# Test the application
curl http://localhost:8080
curl http://localhost:8080/api/health