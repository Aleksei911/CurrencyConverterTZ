FROM python:3.11-alpine3.16

COPY requirements.txt /temp/requirements.txt
COPY converter /converter
WORKDIR /converter
EXPOSE 8000

RUN pip install -r /temp/requirements.txt
