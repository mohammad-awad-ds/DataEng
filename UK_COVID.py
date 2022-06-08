import subprocess
subprocess.check_call(['pip', 'install', 'sklearn'])
import datetime as dt
from datetime import timedelta
import pandas as pd
import numpy as np
from sqlalchemy import create_engine
import psycopg2
import time
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator


def get_list_of_days():
    List_of_days=[]
    for year in range(2020,2022):
        for month in range(1,13):
            for day in range(1,32):
                month=int(month)
                if day <=9:
                    day=f'0{day}'

                if month <= 9 :
                    month=f'0{month}'
                List_of_days.append(f'{month}-{day}-{year}')
    return List_of_days

def get_df_uk_daily(Day):
    DF_i=None
    try: 
        URL_Day=f'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/{Day}.csv'
        DF_day=pd.read_csv(URL_Day)
        DF_day['Day']=Day
        cond=(DF_day.Country_Region=='United Kingdom')&(DF_day.Province_State=='England')
        Selec_columns=['Day','Country_Region', 'Last_Update',
              'Lat', 'Long_', 'Confirmed', 'Deaths', 'Recovered', 'Active',
              'Combined_Key', 'Incident_Rate', 'Case_Fatality_Ratio']
        DF_i=DF_day[cond][Selec_columns].reset_index(drop=True)
    except:
        pass
    return DF_i

def get_files_uk():
    List_of_days = get_list_of_days()
    Start=time.time()
    df_all=[]
    for Day in List_of_days:
        df_all.append(get_df_uk_daily(Day))
    End=time.time()
    Time_in_sec=round((End-Start)/60,2)
    print(f'It took {Time_in_sec} minutes to get all data')

    df_uk=pd.concat(df_all).reset_index(drop=True)
    df_uk['Last_Update']=pd.to_datetime(df_uk.Last_Update, infer_datetime_format=True)  
    df_uk['Day']=pd.to_datetime(df_uk.Day, infer_datetime_format=True)  

    df_uk['Case_Fatality_Ratio']=df_uk['Case_Fatality_Ratio'].astype(float)

    df_uk.head(10)
    return df_uk.copy()

def scale_the_uk_data(ti):
    df_uk = ti.xcom_pull(task_ids="extract_uk_files")
    selected_columns = ['Confirmed','Deaths', 'Recovered', 'Active', 'Incident_Rate','Case_Fatality_Ratio']
    from sklearn.preprocessing import MinMaxScaler

    min_max_scaler = MinMaxScaler()

    df_uk_scaled = pd.DataFrame(min_max_scaler.fit_transform(df_uk[selected_columns]),columns=selected_columns)
    df_uk_scaled['Day']=df_uk.Day
    df_uk_scaled.index=df_uk.Day
    df_uk_scaled.head(3)

    return df_uk_scaled

def plt_generator(ti):
    df_uk_scaled = ti.xcom_pull(task_ids="scale_dataframe")
    selected_columns = ['Confirmed','Deaths', 'Recovered', 'Active', 'Incident_Rate','Case_Fatality_Ratio']
    import matplotlib.pyplot as plt
    df_uk_scaled[selected_columns].plot(figsize=(20,10))
    plt.savefig('/mnt/uk_scoring_report.png')
    df_uk_scaled.to_csv('/mnt/uk_scoring_report.csv')

def Conn_postgres(ti):
    df_uk_scaled = ti.xcom_pull(task_ids="scale_dataframe")
    host="postgres" 
    database="airflow"
    user="airflow"
    password="airflow"
    port='5432'
    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{database}')
    df_uk_scaled.to_sql('uk_scoring_report', engine,if_exists='replace',index=False)

default_args={
    'owner': 'Mohammad',
    'start_date': dt.datetime(2022, 6, 8),
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=2),
}

with DAG(
    'UK_COVID',
    default_args=default_args,
    schedule_interval=timedelta(hours=1),  
    catchup=False,
)as dag:
    begin = BashOperator(task_id='begin', bash_command='echo "start..."')

    collect_files_for_uk = PythonOperator(task_id='extract_uk_files',python_callable=get_files_uk)
    scale_dataframe = PythonOperator(task_id='scale_dataframe',python_callable=scale_the_uk_data)
    plt_csv = PythonOperator(task_id='plt_csv',python_callable=plt_generator)
    loadtoPG = PythonOperator(task_id="loadtoPG", python_callable=Conn_postgres)

    end = BashOperator(task_id='end',bash_command='echo "end.."')

begin >> collect_files_for_uk >> scale_dataframe >> plt_csv >> loadtoPG >> end
