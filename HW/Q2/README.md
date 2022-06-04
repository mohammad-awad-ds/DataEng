#HW1 Q2 Data Engineering 
## Run

```sh
$ docker-compose up
```

| App | Link | Username | Password | 
| ------ | ------ | ------ | ------ |
| JupyterLab | http://localhost:8886/ | - | admin | 
| AirFlow-webServer | http://localhost:8087/ | airflow | airflow | 
| Mongo-express | http://localhost:8088/ | admin | admin |
| pgAdmin| http://localhost:8089/ | admin | admin |


# 

### For Postgres 
Using sql_alchamy library

```
host = "postgres_storage"
database = "csv_db"
user = "admin"
password = "admin"
port = '5432'
engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{database}')

```
### For MongoDB
Using sql_alchamy library

```
client = MongoClient('mongo:27017',
                     username='admin',
                     password='admin'
mongodb = client['admin']
collection = mongodb['admin']
```

Connect to MongoDB, create the DB ='admin' , and Collection = admin


Read From Postgres as PandasDF and save it to CSV FIle. 


Get the CSV file from Postgress and send it to MongoDB



# Complete Pipeline   







