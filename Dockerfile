FROM python:3.11-slim

# Install minimal deps for pygame (may vary by distro)
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        libsdl2-2.0-0 libsdl2-image-2.0-0 libsdl2-mixer-2.0-0 libsdl2-ttf-2.0-0 \
        libportmidi0 libfreetype6 libasound2 && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . /app

# Install pygame if you want to run the GUI inside container
RUN pip install --no-cache-dir pygame

CMD ["python", "tictactoe.py"]
