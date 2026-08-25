# DevOps Portfolio - Terraform
# Author: Luis Martel
# Infrastructure as a Code with Docker

terraform{
  required_providers{
    docker = {
      source = "kreuzwerker/docker"
      version = "~> 3.0"
      }
   }
}

provider "docker" {}

# pull the image 
resource "docker_image" "webapp" {
  name = "luismarteel/devops-webapp:latest"
  keep_locally = false 
}

# create the container
resource "docker_container" "webapp" {
  image = docker_image.webapp.image_id
  name = "devops-webapp-terraform"
  
  ports {
    internal = 8080
    external = 8888
  }

  restart = "unless-stopped"
}
