FROM jupyter/base-notebook:latest
RUN pip install apache-airflow
RUN pip install psycopg2
WORKDIR /usr/src/app
COPY Entregable_3.ipynb /usr/src/app/
EXPOSE 8888
CMD ["airflow", "webserver", "--port", "8080"]
