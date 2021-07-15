FROM python:3.8.10

ENV DJANGO_SETTINGS_MODULE settings.dev

WORKDIR /app
ADD . .

RUN pip install --upgrade pip
RUN pip install -I .
RUN python manage.py collectstatic