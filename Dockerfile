# FROM --platform=linux/amd64 python:3.9
FROM python:3.7.4
ENV PYTHONUNBUFFERED 1
WORKDIR /code

RUN pip install --upgrade pip
RUN pip install Django==3.0
RUN pip install django-mdeditor

# 依存パッケージをrequirements.txtに記述
ADD requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/

