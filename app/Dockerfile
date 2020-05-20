# pull official base image
from python:3.8.0-alpine

# set working directory
workdir /usr/src/app

# set environment variables
env PYTHONDONTWRITEBYTECODE 1
env PYTHONUNBUFFERED 1

# install psycopg2 dependencies
run apk update \
	&& apk add postgresql-dev gcc python3-dev musl-dev libxml2-dev libxslt-dev

# install dependencies
run pip3 install --upgrade pip
copy ./requirements.txt /usr/src/app/requirements.txt
run pip3 install -r requirements.txt
