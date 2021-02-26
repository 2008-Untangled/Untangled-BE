FROM library/postgres

WORKDIR /docker-entrypoint-initdb.d

ENV POSTGRES_USER=username
ENV POSTGRES_PASSWORD=password
ENV POSTGRES_DB=untangled_dev

COPY psql.sh /docker-entrypoint-initdb.d/

FROM python:3.9-slim-buster

ADD . .

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip3 install -r requirements.txt
RUN export DATABASE_URL=postgresql://localhost:5432/untangled_dev
# RUN python manage.py db upgrade
# RUN python3 manage.py db_seed

COPY . .

# RUN chmod u+x ./entrypoint.sh
# ENTRYPOINT ["./entrypoint.sh"]

CMD ["python3", "./python.py"]
