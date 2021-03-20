FROM python:3.9-alpine as base
ENV PYTHONDONTWRITEBYTECODE 1

RUN apk update && \
    apk add --no-cache --virtual .build-deps \
    gcc python3-dev musl-dev \
    postgresql-dev bash


# Using multistage
FROM python:3.9-alpine
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONPATH /app:$PYTHONPATH

COPY --from=base /usr/local/lib/python3.9/site-packages/ /usr/local/lib/python3.9/site-packages
COPY --from=base /usr/local/bin/ /usr/local/bin/

RUN mkdir app

COPY . app/

RUN ls /app/

WORKDIR app

EXPOSE 8000

RUN pip install pipenv && pipenv install

RUN . venv/bin/activate

RUN python manage.py makemigrations && python manage.py migrate && python manage.py collectstatic && python manage.py runserver
