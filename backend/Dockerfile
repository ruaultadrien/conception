FROM python:3.11

WORKDIR /backend

#COPY poetry.lock /backend/
#COPY pyproject.toml /backend/
COPY . /backend

RUN python3 -m pip install --upgrade pip \
    && pip install poetry \
    && poetry install

EXPOSE 8888

CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--reload", "--port", "8888"]
