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
- [ ] Cloud (AWS/GCP(AZURE)
- [x] Observability
- [x] Infrastructure as Code (IAC) 


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
|             FILE               |                     Description                 |
|--------------------------------|-------------------------------------------------|
|        `git/git_notes.md`      |  Add actions and practice with a git            |

## Docker 
|             FILE               |                     Description                 |
|--------------------------------|-------------------------------------------------|
|    /system_info/Dockerfile     |     File docker configuration                   |
|    /system_info/system_info.py |    Script with a system information             |
|  /compose/docker-compose.yaml  |     A yaml configuration for a docker compose   |
|         docker_notes.md        |    a small notations for docker                 | 

## CI - CD 
|             FILE                   |                     Description                 |
|------------------------------------|-------------------------------------------------|
|   tests/test_system.info.py        |  An automated test for a CI/CD practice         |
| .github/workflows/docker-buid-yaml |  CI/CD file automation test for a docker image  |


## Documentation
Complete documentation for each topic covered in this roadmap.

| Document | Description |
|----------|-------------|
| `docs/01-linux.md` | Linux fundamentals and key commands |
| `docs/02-networking.md` | Networking concepts and tools |
| `docs/03-yaml.md` | YAML syntax and use cases |
| `docs/04-git.md` | Git workflow and GitFlow |
| `docs/05-docker.md` | Docker, Compose and Docker Hub |
| `docs/06-kubernetes.md` | Kubernetes objects and kubectl |
| `docs/07-cicd.md` | CI/CD with GitHub Actions |
| `docs/08-observability.md` | Prometheus and Grafana |
| `docs/09-terraform.md` | Infrastructure as Code with Terraform |

## Postmortems
| # | Title |
|---|-------|
| 001 | HTTP/1.0 Incompatibility with Kubernetes Port-Forward |

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
├── tests/
│   └── test_system_info.py
├── .github/
│   └── workflows/
│       └── docker-build.yaml
├── docs/
    └── postmortems
        └── 001_http10_kubernetes_portforward.md
    └──01-linux.md
    └──02-networking.md
    └──03-yaml.md
    └──04_git.md
    └──05_docker.md
    └──06_kubernetes.md
    └──07_cicd.md
    └──08_observability.md
    └──09-terraform.md
├──.gitignore
└── README.md
```

