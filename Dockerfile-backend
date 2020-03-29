FROM python:3.8.2-alpine

COPY . /app

RUN apk add make && \
    cd /app && \
    make install

WORKDIR /app
CMD make run
