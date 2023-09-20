FROM ubuntu:20.04

ENV APP_ROOT /src
ENV CONFIG_ROOT /config
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update --fix-missing -y -qq

ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get install --fix-missing -y --no-install-recommends build-essential software-properties-common apt-utils \
    python3-dev python3-pip python3-setuptools python3-wheel python3-cffi python3-brotli

ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get install --fix-missing -y --no-install-recommends openjdk-8-jre openjdk-8-jdk

RUN rm -r /var/lib/apt/lists /var/cache/apt/archives

RUN mkdir ${CONFIG_ROOT}
RUN pip3 install -U pip
RUN pip install --upgrade pip
COPY requirements.txt ${CONFIG_ROOT}/requirements.txt
RUN pip3 install -r ${CONFIG_ROOT}/requirements.txt

RUN mkdir ${APP_ROOT}
WORKDIR ${APP_ROOT}

ADD . ${APP_ROOT}

EXPOSE 8000
CMD ["python3","manage.py","runserver","0.0.0.0:8000"]

