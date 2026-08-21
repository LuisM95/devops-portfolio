# DevOps Portfolio - Luis Martel

Practical DevOps learning journey through real projects.

## Roadmap Progress
- [x] Linux & Python Scripting
- [x] Networking
- [x] YAML
- [x] Git & GitHub
- [x] Docker
    - [x] Docker compose
- [x] CI/CD 
- [x] Kubernetes
    - [X] Kubernetes - Deployment
    - [x] Kubernetes - Services 
- [ ] Cloud (AWS/GCP(AZURE)
- [ ] Observability
- [ ] Infrastructure as Code (IAC) 


## Scripts 

|             Script             |                    Description                  |
|--------------------------------|-------------------------------------------------|
| `system_info.py`               | Collects system info from a Linux Server        |
| `server_health.py`             | Monitors, Disk, Memory, Process and last Loggin |
| `network_diagnostic.py`        | Connectivity, DNS and HTTP checks script        | 

## YAML 
|             FILE               |                     Description                 |
|--------------------------------|-------------------------------------------------|
|        `server.yaml`           |  RHEL server configuration                      |
|         `app.yaml`             |  "Web Application configuration"                |

## GIT and GITHUB 
|           FILE              |                                 Description                              |
|-----------------------------|--------------------------------------------------------------------------|
|       `git/git_notes.md`    |  Add actions and practice with a git                                     |
|        `.gitignore`         |  file for ignore and exclude files binaries to load on github repositori |

## Docker 
|             FILE               |                     Description                 |
|--------------------------------|-------------------------------------------------|
|    /system_info/Dockerfile     |     File docker configuration                   |
|    /system_info/system_info.py |    Script with a system information             |
|  /compose/docker-compose.yaml  |     A yaml configuration for a docker compose   |
|         docker_notes.md        |    a small notations for docker                 | 

## Docker Images
|             FILE                  |                     Description                 |
|-----------------------------------|-------------------------------------------------|
| `luismarteel/system-info:latest ` |  Automated test for a CICD pipelines            |
|   `luismarteel/devops-webapp `    |  Web application with a Rest Endpoint           |

## CI - CD 
|             FILE                     |                     Description                 |
|--------------------------------------|-------------------------------------------------|
|   `tests/test_system.info.py`        |  An automated test for a CI/CD practice         |
| `.github/workflows/docker-buid-yaml` |  CI/CD file automation test for a docker image  |

## Kubernetes 
|             FILE                   |                     Description                     |
|------------------------------------|-----------------------------------------------------|
|      `Kubernetes/jobs.yaml`        |  Kubernetes job manifest for a system-info script   |
|     `Kubernetes/webapp/app.py`     |  Web Application Source code                        |
|   `kubernetes/webapp/Dockerfile`   |  Docker manifest configuration for webapp           |
| `kubernetes/webapp/deployment.yaml`|  Kubernetes manifest for deployment with 3 replicas |
| `kubernetes/webapp/service.yaml`   |  Kubernetes manifest for load balancing             |


## Structure

```
devops_portfolio/
├── linux/
│   └── scripts/
│       └── system_info.py
|       └── server_health.py
|       └── network_diagnostic.py
├── yaml/
│   └── server.yaml
│   └── app.yaml
├── git/
│   └── git_notes.md
├── docker
│   └── system_info/
│        └── Dockerfile
│        └── system_info.py
│   └── compose/
│        └── docker-compose.yaml
│   └── docker_notes.md
├── kubernetes/
│   └── jobs.yaml
│   └── webapp/
│       └── app.py
│       └── Dockerfile
│       └── deployment.yaml
│       └── service.yaml
├── tests/
│   └── test_system_info.py
├── .github/
│   └── workflows/
│       └── docker-build.yaml
├── .gitignore
└── README.md
```

