
# Converting CSV files Extracted from postgres into JSON and then loading the file into MongoDB all on Apache Airflow by using DAGs.

This is Q2 of homework 1 part of the Data Engineering Course

### 1. After cloning the repo run the prepareproject script to set up the required directories.
### 2. Run 
                        docker-compose up
### 3. Connect to the following services using the following ports and passwords:
| Service    |  Port | User  |Password   |   
|------------|---|---|---|
| Jupyter    |8888 |  - | admin  |   
| pgAdmin    |8089   |  pgadmin@pgadmin.com |  pgadmin123    |
| postgresql | 5432  |  airflow | airflow  |   
| mongoDB |  27017 |  mongo | mongo123  |   
| Airflow |  8087 | airflow  |  airflow |   

-------
-------
In python to connect to database engines use the following parameters with corresponding libraries as done in the DAG python script:
## Connection parameters:
#### Postgresql
- **database**: airflow
- **user**: airflow
- **password**: airflow
- **host**: postgres
- **port**: 5432
----
#### MongoClient
- **localhost**:27017
 - **username**:'mongo'
 - **password**:'mongo123') 

### 4. Setup your postgres server by inputting the values from above into:
![image.png](https://github.com/mohammad-awad-ds/DataEng/blob/main/HomeWork_1/Q2/ImagesGuide/0.%20new%20server.PNG)

![image.png](https://github.com/mohammad-awad-ds/DataEng/blob/main/HomeWork_1/Q2/ImagesGuide/0.1%20server%20add.PNG)

Get the host address from:
![image.png](https://github.com/mohammad-awad-ds/DataEng/blob/main/HomeWork_1/Q2/ImagesGuide/0.2%20serverip.PNG)

You can upload your data manually or using python as provided in the notebook in the notebooks directory.

### 5. Check pyhton script in the dag folder:
![image.png](https://github.com/mohammad-awad-ds/DataEng/blob/main/HomeWork_1/Q2/ImagesGuide/code%20in%20dag%20folder.PNG)
![image.png](https://github.com/mohammad-awad-ds/DataEng/blob/main/HomeWork_1/Q2/ImagesGuide/snippit%201.PNG)
![image.png](https://github.com/mohammad-awad-ds/DataEng/blob/main/HomeWork_1/Q2/ImagesGuide/snippit%202.PNG)
![image.png](https://github.com/mohammad-awad-ds/DataEng/blob/main/HomeWork_1/Q2/ImagesGuide/Snippit%203%20dags.PNG)

### 6. Connect to airflow using localhost:8087 and turn on the dag
![image.png](https://github.com/mohammad-awad-ds/DataEng/blob/main/HomeWork_1/Q2/ImagesGuide/Dag%20homepage.PNG)
## Click on DAG name to view it 
![image.png](https://github.com/mohammad-awad-ds/DataEng/blob/main/HomeWork_1/Q2/ImagesGuide/airflow%20tree%20view.PNG)
## Green outline indicates the successful completion of the DAG task
![image.png](https://github.com/mohammad-awad-ds/DataEng/blob/main/HomeWork_1/Q2/ImagesGuide/AirFlow%20Success%20pipeline.PNG)

# I hope you find this useful!


