FROM python:3.9-alpine as base
ENV PYTHONDONTWRITEBYTECODE 1

RUN apk update && \
    apk add --no-cache --virtual .build-deps \
    build-base gcc python3-dev musl-dev \
    postgresql-dev bash

RUN pip install pipenv psycopg2


# Using multistage
FROM python:3.9-alpine
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONPATH /app:$PYTHONPATH

COPY --from=base /usr/local/lib/python3.9/site-packages/ /usr/local/lib/python3.9/site-packages
COPY --from=base /usr/local/bin/ /usr/local/bin/
COPY --from=base /usr/bin/ /usr/bin/

RUN apk update && apk add postgresql-libs postgresql-dev

RUN mkdir app

COPY . app/

WORKDIR app

EXPOSE 8000

RUN pipenv install --deploy --system --dev

ENTRYPOINT ["python", "manage.py"]

CMD ["runserver", "0.0.0.0:8000"]
