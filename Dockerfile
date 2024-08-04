FROM python:3.12-slim-bullseye

RUN apt-get update
RUN apt-get install -y python3-dev build-essential libpq-dev
#pip req
RUN pip install --upgrade pip
RUN pip install virtualenv && python -m virtualenv /opt/venv


ENV PATH="/opt/venv/bin:$PATH"

ADD ./requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

COPY . /srv/app
WORKDIR /srv/app

