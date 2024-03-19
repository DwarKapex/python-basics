# syntax=docker/dockerfile:1-labs
ARG BASE_IMAGE=python:3.11.7-bookworm

FROM ${BASE_IMAGE}

RUN pip install "poetry==1.7.1"
RUN poetry config virtualenvs.create false

WORKDIR /app

COPY . .
RUN poetry install --no-root

CMD [ "uvicorn", "main:app", "--host=0.0.0.0", "--port=8000" ]

EXPOSE 8000
