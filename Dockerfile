FROM python:3.9.5-slim-buster

ADD . ./app

WORKDIR /app

RUN pip3 install -r requirements.txt

EXPOSE 5000

CMD [ "python","app.py" ]