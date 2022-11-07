FROM ubuntu
RUN apt update -y \
    && apt install python3 -y \
    && apt install python3-pip -y \
    && apt install libpq-dev \
    && pip install psycopg2
WORKDIR /app
COPY ./pgsql.py .
CMD ["python3","-u","/app/pgsql.py"]
