FROM python:3.11-slim-buster
LABEL authors="lyapin"

WORKDIR /app

RUN apt-get update && apt-get install -y gcc build-essential

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip  \
    && pip install --no-cache-dir -r ./requirements.txt \
    && pip install websockets==12.0 uvicorn[standard]

COPY . .


ENV PYTHONPATH "${PYTHONPATH}:${APP_DIR}"