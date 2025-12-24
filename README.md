# Distributed Turn-Based State Engine

This repository contains a compact Tic-Tac-Toe state engine and a simple UI used as a demonstration project. The repository has been updated to align with a Senior Software Engineer profile focused on cloud-native systems, Kubernetes, and event-driven architectures.

**Profile:** Senior Software Engineer — expertise in AWS/Azure, Kubernetes, containerization, and event-driven systems (Kafka/EventBridge).

**What I changed:**
- Removed local Jupyter notebook to avoid accidental leakage of secrets or environment-specific outputs.
- Refactored `tictactoe.py` into a module-friendly form with a runnable `main()` guard for safer imports.
- Added `.gitignore` and a lightweight `Dockerfile` to demonstrate containerization.

**Highlights / Technologies:**
- Python 3.11
- Containerization: Dockerfile included
- Cloud readiness: notes and run commands for container + Kubernetes
- Event-driven readiness: the engine is structured so game/state events can be emitted to message brokers (Kafka, SNS/SQS, EventGrid)

Quick start (local):

1. Create a virtual environment and install dependencies (if you use pygame for the GUI):

```
python -m venv .venv
.venv\Scripts\activate
pip install -U pip
pip install pygame
```

2. Run locally:

```
python tictactoe.py
```

Build and run with Docker (example):

```
docker build -t tictactoe:latest .
docker run --rm -it tictactoe:latest
```

Kubernetes / Cloud guidance:
- Containerize the app (see Dockerfile) and deploy behind a simple service. For event-driven architectures, run the game engine headless and publish game-state events to Kafka / Kinesis / EventGrid using a small sidecar or integrated producer.

Security note:
- Jupyter notebooks were removed from the repository to reduce risk of inadvertently exposing credentials or secrets. Keep secrets out of the repo and use environment variables or a secrets manager (AWS Secrets Manager / Azure Key Vault).

If you want, I can:
- Add a small HTTP wrapper (`Flask`/`FastAPI`) to expose the engine as a microservice for Kubernetes deployments.
- Add CI/CD suggestions (GitHub Actions) to build and scan containers and push images to ECR/ACR.
