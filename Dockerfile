FROM python:3.10-alpine3.18

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

RUN pip install pipenv

COPY . .

RUN pipenv install --deploy --system --ignore-pipfile

WORKDIR /usr/src/app/app

ENTRYPOINT ["./entrypoint.sh"]
