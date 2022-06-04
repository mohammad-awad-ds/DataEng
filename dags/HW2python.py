import pandas as pd
import numpy as np
from sqlalchemy import create_engine
import psycopg2
import time
import datetime as dt
from datetime import timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator

default_args={
    'owner': 'admin',
    'start_date': dt.datetime(2022, 6, 4),
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=3),
}

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
        print("Running")
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
    df_uk = ti.xcom_pull(task_ids="collect_files_for_uk")
    selected_columns = ['Confirmed','Deaths', 'Recovered', 'Active', 'Incident_Rate','Case_Fatality_Ratio']
    from sklearn.preprocessing import MinMaxScaler

    min_max_scaler = MinMaxScaler()

    df_uk_scaled = pd.DataFrame(min_max_scaler.fit_transform(df_uk[selected_columns]),columns=selected_columns)
    df_uk_scaled['Day']=df_uk.Day
    df_uk_scaled.index=df_uk.Day
    df_uk_scaled.head(3)

    return df_uk_scaled

def create_plt_csv(ti):
    df_uk_scaled = ti.xcom_pull(task_ids="scale_dataframe")
    selected_columns = ['Confirmed','Deaths', 'Recovered', 'Active', 'Incident_Rate','Case_Fatality_Ratio']
    import matplotlib.pyplot as plt
    df_uk_scaled[selected_columns].plot(figsize=(20,10))
    plt.savefig('/mnt/uk_scoring_report.png')
    df_uk_scaled.to_csv('/mnt/uk_scoring_report.csv')

def df_to_db(ti):
    df_uk_scaled = ti.xcom_pull(task_ids="scale_dataframe")
    host="postgres" 
    database="deproject"
    user="admin"
    password="admin"
    port='5432'
    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{database}')
    df_uk_scaled.to_sql('uk_scoring_report', engine,if_exists='replace',index=False)

with DAG(
    'HW2',
    default_args=default_args,
    schedule_interval=timedelta(hours=1),  
    catchup=False,
)as dag:
    starting_point = BashOperator(task_id='starting_point', bash_command='echo "I am starting the DAG"')
    installing_modules = BashOperator(task_id='installing_modules', bash_command='pip install sklearn matplot logging')
    collect_files_for_uk = PythonOperator(task_id='collect_files_for_uk',python_callable=get_files_uk)
    scale_dataframe = PythonOperator(task_id='scale_dataframe',python_callable=scale_the_uk_data)
    create_plot_and_csv = PythonOperator(task_id='create_plot_and_csv',python_callable=create_plt_csv)
    send_dataframe_to_Postgres = PythonOperator(task_id="send_dataframe_to_Postgres", python_callable=df_to_db)
    ending_point = BashOperator(task_id='ending_point',bash_command='echo "Complete"')

starting_point >> installing_modules >> collect_files_for_uk >> scale_dataframe >> create_plot_and_csv >> send_dataframe_to_Postgres >> ending_point
