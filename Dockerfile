FROM python:3.10.13-alpine

# Создаем папку и переходим в неё.
WORKDIR /app

RUN pip install --upgrade --no-cache-dir pip && pip install poetry --no-cache-dir;

# Копируем `pyproject.toml` в текущую папку.
COPY pyproject.toml poetry.lock  /app/

# Устанавливаем зависимости
RUN poetry config virtualenvs.create false && \
    poetry install --only main --no-interaction --no-ansi --no-cache;

COPY . .

#WORKDIR /app


RUN chmod +x run.sh


WORKDIR /app/coworkingspace
