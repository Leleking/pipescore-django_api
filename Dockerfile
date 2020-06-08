# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM  python:3.6.10-alpine

RUN apk update \
    && apk add --no-cache --virtual bash \
    && apk add gcc \
    && apk add musl-dev \
    && apk add linux-headers \
    && apk add jpeg-dev \
    && apk add zlib-dev \
    && apk add mariadb-dev \
    && apk add libffi-dev \
    && apk add libxml2-dev libxslt-dev


# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# create root directory for our project in the container
RUN mkdir /api

# Set the working directory to /api
WORKDIR /api

# Copy the current directory contents into the container at /music_service
COPY . /api/




# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip \
    && pip install -r requirements.txt
