FROM python:3.13

RUN apt-get update && apt-get install -y libpq-dev gcc git &&\
    curl -sSL https://install.python-poetry.org | python3 - && \
    export PATH="$HOME/.local/bin:$PATH"

ENV PATH="/root/.local/bin:$PATH"

WORKDIR /app

COPY . .

EXPOSE 9898

CMD sh -c "poetry install && poetry run python run.py"
