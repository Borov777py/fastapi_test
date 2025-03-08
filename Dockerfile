FROM python:3.12

WORKDIR /app

COPY . /app
RUN pip install poetry
RUN poetry config virtualenvs.in-project true
RUN poetry install --no-root

CMD [ "poetry", "run", "python", "/app/main.py" ]