FROM python:3.9-slim-buster

ADD . .

RUN pip3 install -r requirements.txt
RUN psql -c 'create database untangled-db;' -U postgres
RUN python manage.py db upgrade
RUN python manage.py db_seed

CMD ["python3", "run.py"]