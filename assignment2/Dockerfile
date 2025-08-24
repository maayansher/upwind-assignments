FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    net-tools \
    curl \
    strace \
    inotify-tools \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY malware.py malware.py
COPY generate_report.py generate_report.py
CMD ["python", "malware.py"]
