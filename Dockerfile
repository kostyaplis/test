FROM python:3.11-slim

WORKDIR /app

COPY process.py logger.conf ./

ENTRYPOINT ["python"]
CMD ["process.py", "lines.txt"]
