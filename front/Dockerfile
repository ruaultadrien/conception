FROM python:3.11

WORKDIR /front

#COPY poetry.lock /front
#COPY pyproject.toml /front
COPY . /front


RUN python3 -m pip install --upgrade pip \
    && pip install poetry \
    && poetry install

CMD ["poetry", "run", "streamlit", "run", "Conception.py"]