FROM python:3.11-slim

WORKDIR /app

COPY process.py logger.conf ./

ENTRYPOINT ["python", "process.py"]
