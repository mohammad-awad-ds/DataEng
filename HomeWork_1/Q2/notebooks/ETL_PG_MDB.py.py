#loading libraries
def load_depend():
    import datetime as dt
    from datetime import timedelta
    from airflow import DAG
    from airflow.operators.bash_operator import BashOperator
    from airflow.operators.python_operator import PythonOperator
    import pandas as pd
    import json
    import pymongo
    from faker import Faker
    import psycopg2 
    from sqlalchemy import create_engine


default_args = {
    'owner': 'Mohammad',
    'start_date': dt.datetime(2022, 6, 8),
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=5),
}

with DAG('Dependencies',
         default_args=default_args,
         schedule_interval=timedelta(minutes=1),  
         catchup=False) as dag:
    print_starting = BashOperator(task_id='starting',
                                  bash_command='echo "Setting up dependencies..."')
    dependency = PythonOperator(task_id='Dependencies', 
                             python_callable=load_depend)
    print_closing = BashOperator(task_id='closing',
                                  bash_command='echo "closing..."')
    print_starting>>dependency>>print_closing