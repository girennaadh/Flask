FROM python:3.7.11-alpine3.13

ENV INSTALL_PATH /flaskpostgresapp
RUN mkdir -p $INSTALL_PATH

WORKDIR $INSTALL_PATH

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN apk update \
  && apk add --virtual .build-deps gcc python3-dev musl-dev g++ \
  && apk add postgresql-dev \
  && pip install psycopg2

RUN pip install -r requirements.txt
RUN apk del .build-deps gcc musl-dev g++
COPY . .

ENTRYPOINT ["python"]

CMD ["app.py"]