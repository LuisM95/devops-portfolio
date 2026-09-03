# Yaml Documentation

## YAML Definition
Yaml is not a markup language used in configuring project files with which it can be used to define infrastructure configuration, docker or deployments in kubernetes.

## YAML in DevOps 
Yaml in DevOps is used to configure files that allow you to create CI/CD pipelines for software development, deployments, testing an release of software features.

## Data Types on Yaml 
```
- Integers 
- Strings 
- Float 
- Boolean
- null
```

## Important Rule
The Yaml's Golden Rule is indentation and that  hierarchical structure is define exclusively by space

## Cases of Use YAML
Yaml can be used with all programming languages, it has use cases such as: automation, orchestration, and configuration management; yaml files serve as blueprint within DevOps practices.

```
- IaC 
- Automation
- Orchestration
- Distributions 
- CI/CD Pipelines Configuration
- Docker
- Kubernetes
- Github Actions 
- ETC.
```

## Practical Example.
``` yaml
#Docker Compose example
services:
  webapp: 
    images: luismarteel/devops-webapp:latest
    ports: 
      - "8080:8080"
    restart: unless-stoped
``` 
