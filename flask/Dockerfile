FROM python:3.7.11-stretch

WORKDIR /app

ADD . .

RUN pip install -r requirements.txt

CMD ["uwsgi", "app.ini"]