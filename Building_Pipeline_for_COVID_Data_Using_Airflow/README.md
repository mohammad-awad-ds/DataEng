# Build a pipeline for JHU COVID data for the UK using Airflow

--------------------

## **Note**: The workflow is extremely slow at the second stage when the extraction of data begins using the time library.

--------------

#### Data URL:
https://github.com/CSSEGISandData/COVID-19

#### Notebook to be automated:
https://bit.ly/3ugP8Qg

Build an AirFlow DAG for all pipelines and filter on United Kingdom (UK).

● The output of the pipelines should be

■ uk_scoring_report.png

■ uk_scoring_report.csv

■ PostgreSQL table uk_scoring_report

### 1. After cloning the repo run the prepareproject script to set up the required directories.
### 2. Run 
                        docker-compose up

### Place the Python script "UK_COVID.py" in the dag folder

### 3. Connect to the following services using the following ports and passwords:
| Service    |  Port | User  |Password   |   
|------------|---|---|---|
| Jupyter    |8888 |  - | admin  |   
| PostgreSQL | 5432  |  airflow | airflow  |   
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


### 4. Check Python script in the dag folder:
![image.png](https://github.com/mohammad-awad-ds/Data_Engineering/blob/main/Building_Pipeline_for_COVID_Data_Using_Airflow/ImagesGuide/Snippit%201.PNG)
![image.png](https://github.com/mohammad-awad-ds/Data_Engineering/blob/main/Building_Pipeline_for_COVID_Data_Using_Airflow/ImagesGuide/Snippit%202.PNG)
![image.png](https://github.com/mohammad-awad-ds/Data_Engineering/blob/main/Building_Pipeline_for_COVID_Data_Using_Airflow/ImagesGuide/Snippit%203.PNG)
![image.png](https://github.com/mohammad-awad-ds/Data_Engineering/blob/main/Building_Pipeline_for_COVID_Data_Using_Airflow/ImagesGuide/Snippit%204.PNG)
### 5. Connect to Airflow using localhost:8087 and turn on the DAG
![image.png](https://github.com/mohammad-awad-ds/Data_Engineering/blob/main/Building_Pipeline_for_COVID_Data_Using_Airflow/ImagesGuide/Airflow%20dag%20home.PNG)
## Click on DAG name to view it 
![image.png](https://github.com/mohammad-awad-ds/Data_Engineering/blob/main/Building_Pipeline_for_COVID_Data_Using_Airflow/ImagesGuide/dag%20tree%20view.PNG)
## Green outline indicates the successful completion of the DAG task, while light green is still running.
![image.png](https://github.com/mohammad-awad-ds/Data_Engineering/blob/main/Building_Pipeline_for_COVID_Data_Using_Airflow/ImagesGuide/dag%20graph%20view.PNG)
