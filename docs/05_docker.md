# Docker Documentation

## What is Docker and what problem does it  solve?
Docker is a software development tool that is used to containerize applications. 
The problem it solve is to containerize the applications so that they runs regardless of the platform on the which they are hosted, and help to make better use of the available infrastructure.

## Image vs Container
The image is a ready-only script or template that defines the container. The image contains the code to be executed, including definitions, libraries or dependencies.

A container is the instantiated (running) docker image.

## Dockerfile - Main Instructions 
```
FROM      ->  Base image from where it starts (for example: python 3.11-slim)
WORKDIR   ->  Working directory inside the container
COPY      ->  Copy files from your PC to the container
RUN       ->  execute commands during image construction 
EXPOSE    ->  Declare port that the app use
CMD       ->  Command that is executed when the container boots.
```

## Docker Compose 

It's a tool for define and run multiple containers in a single docker-compose file. With a single `docker compose up` you lift the entire stack 

## Essential Commands 
``` BASH 
docker build -t <name>:<tag>  ~  Build and image
docker run image              ~  Create and run a container
docker ps                     ~  List containers running 
docker ps -a                  ~  List all containers
docker stop <name>            ~  Stop a container
docker images                 ~  List a local images
docker push <name>            ~  Upload image to DockerHub 
docker pull <name>            ~  Download image from DockerHub 
docker logs <name>            ~  View container logs 
docker compose up -d          ~  Start the stack in background 
docker compose down           ~  Stop and delete containers 
```

## Docker Hub 

Public Registry where Docker images are stored and shared. It's like Github but for images. You can upload your own images and download those from the community.
