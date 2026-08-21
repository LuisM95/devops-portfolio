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
- [ ] Kubernetes
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
├── .gitignore
└── README.md
```

