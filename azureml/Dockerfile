FROM python:3.11-slim

COPY ./pyproject.toml /workdir/pyproject.toml

WORKDIR /workdir

# Install dependencies
RUN pip install --upgrade pip
RUN pip install poetry

RUN poetry config virtualenvs.create false

RUN poetry install
