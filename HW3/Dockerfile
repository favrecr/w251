FROM ubuntu

RUN apt update

ENV DEBIAN_FRONTEND=noninteractive

RUN apt install -y python-pip

RUN pip install paho-mqtt
RUN pip install ibm-cos-sdk

WORKDIR /
COPY upload.py /