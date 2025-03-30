FROM python:3.13

RUN apt-get update && apt-get install -y libpq-dev gcc git && \
    rm -rf /var/lib/apt/lists/* && \
    curl -sSL https://install.python-poetry.org | python3 -

ENV PATH="/root/.local/bin:$PATH"

WORKDIR /app

COPY pyproject.toml poetry.lock .env ./
RUN poetry install --no-root

COPY . .

EXPOSE 9898

CMD ["poetry", "run", "python", "run.py"]
