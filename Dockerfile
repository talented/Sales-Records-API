FROM python:3.6-alpine
MAINTAINER Talented

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app



# Install dependencies
COPY requirements.txt .

RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev

RUN pip3 install -r ./requirements.txt
RUN apk del .tmp-build-deps

COPY . /app



