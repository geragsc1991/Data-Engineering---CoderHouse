from datetime import datetime, timedelta
from email.policy import default
from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator


default_args={
    'owner': 'DavidBU',
    'retries':5,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    default_args=default_args,
    dag_id='dag_con_conexion_postgres',
    description= 'Entregable 3',
    start_date=datetime(2023,12,22),
    schedule_interval='0 0 * * *'
    ) as dag:
    task1= PostgresOperator(
        task_id='crear_tabla_postgres',
        postgres_conn_id= 'postgres_localhost',
        sql="""
            create table if not exists Aapl(
                Date date,
                Open decimal,
                High decimal,
                Low  decimal,
                Close decimal,
                Volume decimal,
                "Ex-Dividend" decimal,
                "Split Ratio" decimal,
                "Adj. Open" decimal,
                "Adj. High" decimal,
                "Adj. Low" decimal,
                "Adj. Close" decimal,
                "Adj. Volume" decimal
            )
        """
    )
    task2 = PostgresOperator(
        task_id='insertar_en_tabla',
        postgres_conn_id='postgres_localhost',
        sql="""
            COPY Aapl FROM 'C:/Users/sanch/OneDrive/Documentos/GitHub/Entregable 3/AAPL.csv' WITH (FORMAT CSV, HEADER true, DELIMITER ',');
        """
)

    task1 >> task2