FROM python:3.11

WORKDIR /app

COPY poetry.lock /app
COPY pyproject.toml /app

RUN python3 -m pip install --upgrade pip \
    && pip install poetry \
    && poetry install

CMD ["poetry", "run", "streamlit", "run", "main.py"]