FROM python:3

ENV PYTHONUNBUFFERED 1

RUN mkdir /code

WORKDIR /code

COPY . /code/

COPY ./requirements.txt /code/requirements.txt

RUN pip install -r requirements.txt
