# Distributed Turn-Based State Engine

This repository contains a compact Tic-Tac-Toe state engine and a simple UI used as a demonstration project. 

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
