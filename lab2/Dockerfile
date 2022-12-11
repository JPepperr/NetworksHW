# syntax=docker/dockerfile:1

FROM python:3.8

WORKDIR /find_mtu

RUN apt-get update -y
RUN apt-get install -y iputils-ping

COPY . .

ENTRYPOINT ["python3", "main.py"]
