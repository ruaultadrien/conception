FROM python:3.11-slim

COPY . /workdir

WORKDIR /workdir

# Install dependencies
RUN pip install --upgrade pip
RUN pip install poetry
RUN poetry install
