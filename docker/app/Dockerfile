FROM python:3.12

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . /app
RUN pip install poetry
RUN poetry config virtualenvs.in-project true --local
RUN poetry install --no-root

CMD [ "poetry", "run", "python", "/app/main.py" ]