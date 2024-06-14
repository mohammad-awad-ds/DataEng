#loading libraries
import subprocess
subprocess.check_call(['pip', 'install', 'pymongo'])
import datetime as dt
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
import pandas as pd
import json
from pymongo import MongoClient
from sqlalchemy import create_engine

#Create sql_engine
def ExtractfromPG():
    #Connect to postgres
    host="postgres" 
    database="airflow"
    user="airflow"
    password="airflow"
    port='5432'
    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{database}')

    #Extract csv from postgres
    DF=pd.read_sql("SELECT * FROM users2022" , engine);
    DF.to_csv('data.csv',index=False)

def TransformtoJSON():
    #Read CSV file
    df=pd.read_csv('data.csv')
    
    #Transform csv into json format 
    df=df.to_json('./data.json', orient='records')
    alldata={}
    alldata['records']=[]
    with open('data.json','rb') as f:
        data=json.load(f)
        alldata['records']=data
    
    output=open('alldata.json','w')
    json.dump(alldata,output)
    output.close()

def LoadtoMongo():
    #Read JSON
    with open('alldata.json','rb') as f:
        alldata=json.load(f)

    #Connect to Mongo
    client = MongoClient('mongo:27017', username='mongo', password='mongo123')
    db = client['Mohammad']

    #Upload to MongoDB
    articles = db.random
    result = articles.insert_one(alldata)


default_args = {
    'owner': 'Mohammad',
    'start_date': dt.datetime(2022, 6, 8),
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=5),
}

with DAG('ETL_PG_MDB',
         default_args=default_args,
         schedule_interval=dt.timedelta(minutes=1),  
         catchup=False) as dag:

    print_starting = BashOperator(task_id='starting',
                                  bash_command='echo "Begin ETL..."')

    Extract = PythonOperator(task_id='ExtractCSV',
                             python_callable=ExtractfromPG)
    Transform = PythonOperator(task_id='TransformJSON',
                             python_callable=TransformtoJSON)
    Load = PythonOperator(task_id='LoadMongo',
                             python_callable=LoadtoMongo)

    print_closing = BashOperator(task_id='closing',
                                  bash_command='echo "ETL done..."')

    print_starting>>Extract>>Transform>>Load>>print_closing