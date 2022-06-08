#JHU data to APACHE AIRFLOW
import pandas as pd 
import time 
import matplotlib.pyplot as plt 
import matplotlib
from sklearn.preprocessing import MinMaxScaler




    # Get all daily data for UK directly from github repo up to now
def Extract()
    Day='01-01-2021'
    URL_Day=f'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/{Day}.csv'
    DF_day=pd.read_csv(URL_Day)
    DF_day['Day']=Day
    cond=(DF_day.Country_Region=='United Kingdom')&(DF_day.Province_State=='England')
    Selec_columns=['Day','Country_Region', 'Last_Update',
           'Lat', 'Long_', 'Confirmed', 'Deaths', 'Recovered', 'Active',
           'Combined_Key', 'Incident_Rate', 'Case_Fatality_Ratio']
    DF_i=DF_day[cond][Selec_columns].reset_index(drop=True)

def daysList():
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

def Get_DF_i(Day):
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
    #print(f'{Day} is not available!')
        pass
    return DF_i

def processTime():
    Start=time.time()
    DF_all=[]
    for Day in List_of_days:
        DF_all.append(Get_DF_i(Day))
    End=time.time()
    Time_in_sec=round((End-Start)/60,2)
    print(f'It took {Time_in_sec} minutes to get all data')
    
def ukDF():
    DF_UK=pd.concat(DF_all).reset_index(drop=True)
    # Create DateTime for Last_Update
    DF_UK['Last_Updat']=pd.to_datetime(DF_UK.Last_Update, infer_datetime_format=True)  
    DF_UK['Day']=pd.to_datetime(DF_UK.Day, infer_datetime_format=True)  

    DF_UK['Case_Fatality_Ratio']=DF_UK['Case_Fatality_Ratio'].astype(float)
