# Converting CSV files Extracted from PostgreSQL into JSON and then loading the file into MongoDB all on Apache Airflow by using DAGs.


### 1. After cloning the repo run the prepareproject script to set up the required directories.
### 2. Run 
                        docker-compose up
### 3. Connect to the following services using the following ports and passwords:
| Service    |  Port | User  |Password   |   
|------------|---|---|---|
| Jupyter    |8888 |  - | admin  |   
| pgAdmin    |8089   |  pgadmin@pgadmin.com |  pgadmin123    |
| PostgreSQL | 5432  |  airflow | airflow  |   
| MongoDB    |  27017 |  mongo | mongo123  |   
| Airflow    |  8087 | airflow  |  airflow |   

-------
-------
In Python to connect to database engines use the following parameters with corresponding libraries as done in the DAG Python script:
## Connection parameters:
#### PostgreSQL
- **database**: airflow
- **user**: airflow
- **password**: airflow
- **host**: postgres
- **port**: 5432
----
#### MongoClient
- **localhost**:27017
- **username**: 'mongo'
- **password**: 'mongo123' 

### 4. Setup your PostgreSQL server by inputting the values from above into:
![image.png](https://github.com/mohammad-awad-ds/Data_Engineering/blob/main/ETL_Work/CSV_from_Postgres_into_JSON_Loaded_into_MongoDB_Using_Apache_Airflow/ImagesGuide/0.%20new%20server.PNG)

![image.png](https://github.com/mohammad-awad-ds/Data_Engineering/blob/main/ETL_Work/CSV_from_Postgres_into_JSON_Loaded_into_MongoDB_Using_Apache_Airflow/ImagesGuide/0.1%20server%20add.PNG)

Get the host address from:
![image.png](https://github.com/mohammad-awad-ds/Data_Engineering/blob/main/ETL_Work/CSV_from_Postgres_into_JSON_Loaded_into_MongoDB_Using_Apache_Airflow/ImagesGuide/0.2%20serverip.PNG)

You can upload your data manually or using Python as provided in the notebook in the notebooks directory.

### 5. Check Python script in the dag folder:
![image.png](https://github.com/mohammad-awad-ds/Data_Engineering/blob/main/ETL_Work/CSV_from_Postgres_into_JSON_Loaded_into_MongoDB_Using_Apache_Airflow/ImagesGuide/code%20in%20dag%20folder.PNG)
![image.png](https://github.com/mohammad-awad-ds/Data_Engineering/blob/main/ETL_Work/CSV_from_Postgres_into_JSON_Loaded_into_MongoDB_Using_Apache_Airflow/ImagesGuide/snippit%201.PNG)
![image.png](https://github.com/mohammad-awad-ds/Data_Engineering/blob/main/ETL_Work/CSV_from_Postgres_into_JSON_Loaded_into_MongoDB_Using_Apache_Airflow/ImagesGuide/snippit%202.PNG)
![image.png](https://github.com/mohammad-awad-ds/Data_Engineering/blob/main/ETL_Work/CSV_from_Postgres_into_JSON_Loaded_into_MongoDB_Using_Apache_Airflow/ImagesGuide/Snippit%203%20dags.PNG)

### 6. Connect to Airflow using localhost:8087 and turn on the DAG
![image.png](https://github.com/mohammad-awad-ds/Data_Engineering/blob/main/ETL_Work/CSV_from_Postgres_into_JSON_Loaded_into_MongoDB_Using_Apache_Airflow/ImagesGuide/Dag%20homepage.PNG)
## Click on DAG name to view it 
![image.png](https://github.com/mohammad-awad-ds/Data_Engineering/blob/main/ETL_Work/CSV_from_Postgres_into_JSON_Loaded_into_MongoDB_Using_Apache_Airflow/ImagesGuide/airflow%20tree%20view.PNG)
## Green outline indicates the successful completion of the DAG task
![image.png](https://github.com/mohammad-awad-ds/Data_Engineering/blob/main/ETL_Work/CSV_from_Postgres_into_JSON_Loaded_into_MongoDB_Using_Apache_Airflow/ImagesGuide/AirFlow%20Success%20pipeline.PNG)

