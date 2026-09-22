# Terraform Documentation 

## What is Terraform?
Terraform is the most popular Infrastructure as a Code (IaC) tool. It allows you to define provision and manage infrastructure using code files instead of manual clicks in a cloud console.

## Why Terraform? 
Without terraform:
- Manual configuration in cloud console.
- Not reproducible - hard to recreate the same environment.
- No version control for infraestructure.
- Human errors in configuration 

With terraform:
- Infrastructure define as code (.tf files).
- Reproducible - same result every time.
- Version controlled in git.
- Automated and consistent.

## Key Concepts 

### Providers.
connectors to each plaftorm.

```hcl
providers "aws" {}         # Amazon Web services 
providers "google" {}      # Google Cloud Platform
providers "azurerm" {}     # Microsoft Azure.
providers "docker" {}      # Docker
providers "kubernetes" {}  # Kubernetes
```

### Resources.
Infrastructure objects you create
```hcl
resource "docker_container" "webapp" {
    image = "luismarteel/devops-webapp:latest"
    name = "devops-webapp-terraform"
    ports = {
        internal = 8080
        external = 8888
    }
} 
```

### State
Terraform save the state of your infrastructure in `terraform.tfstate`. This file is terraform's memory - it knows what already exists.

**Important:** Never commit `terraform.tfstate` to Git. In production, use remote state (S3, GCP, Terraform Cloud).

### Idempotence.

You can run `terraform apply` 1000 time and the result is always the same:
- First time -> create resources.
- Second time (no change) -> does nothing
- Third time (with change) -> only modifies what change.

## The 4 Core Commands 
```bash 
terraform init     # Initialize project, download providers 
terraform plan     # Show what will be created/modified/destroyed 
terraform apply    # Apply the changes (create infraestructure)
terraform destroy  # Destroy all infraestructure.
```

## Terraform Plan Output

- Resources will be created (green)
- Resources will be destroy (red)
- Resources will be modified (yellow)

**Plan: 2 to add, 0 to change, 0 to destroy** 


## Project Used in Portfolio
```hcl
# main.tf
terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0"
    }
  }
}

provider "docker" {}

resource "docker_image" "webapp" {
  name         = "luismarteel/devops-webapp:latest"
  keep_locally = false
}

resource "docker_container" "webapp" {
  image = docker_image.webapp.image_id
  name  = "devops-webapp-terraform"
  ports {
    internal = 8080
    external = 8888
  }
  restart = "unless-stopped"
}
```

## Files to add to .gitignore
```gitignore
.terraform/
.terraform.lock.hcl
terraform.tfstate
terraform.tfstate.backup
*.tfvars
crash.log
```

  
