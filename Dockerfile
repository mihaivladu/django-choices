FROM python:latest
ENV PYTHONBUFFERED 1
RUN mkdir /app
WORKDIR /app
ADD requirements.txt /app/
RUN pip install -r requirements.txt
ADD . /app/