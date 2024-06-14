
# Converting CSV files into JSON using NIFI on Docker 

This is Q1 of homework 1 part of the Data Engineering Course

## The following are the instructions to run this workflow successfully
### 1. Download the repo to the desired location and run "dir_creator.sh" script to prepare the required directories for docker volumes.
### 2. Drop the users.csv file into the database directory.
### 3. On the terminal cd to the one chosen in step 2 and run: 
                                        docker-compose up
### 4. Open your browser and connect to 
                                        localhost:8080/NIFI
### 5. As in the picture below drag and drop the presaved template and choose "CSVtoJSON_Template_Mohammad"
![alt text](https://github.com/mohammad-awad-ds/DataEng/blob/main/HomeWork_1/Q1/Guide_Images/drop%20template.png)

### 6. Turn on services from the left-hand side panel by pressing on the gear icon and then pressing the bolts
![alt text](https://github.com/mohammad-awad-ds/DataEng/blob/main/HomeWork_1/Q1/Guide_Images/workflow.PNG)
![alt text](https://github.com/mohammad-awad-ds/DataEng/blob/main/HomeWork_1/Q1/Guide_Images/B-0%20turn%20on%20services.PNG)

### 7. Set up the correct directory for you by changing it in the GetFile and PutFile processes.
![alt text](https://github.com/mohammad-awad-ds/DataEng/blob/main/HomeWork_1/Q1/Guide_Images/directory.PNG)

### 8. Now you can run the work flow and check the database directory to find your JSON file.

#### Note: this workflow works on the provided users.csv file schema: 
{
  "type": "record",
  "name": "UserRecord",
  "fields" : [
    {"name": "id", "type": "long"},
    {"name": "title", "type": ["null", "string"]},
    {"name": "first", "type": ["null", "string"]},
    {"name": "last", "type": ["null", "string"]},
    {"name": "street", "type": ["null", "string"]},
    {"name": "city", "type": ["null", "string"]},
    {"name": "state", "type": ["null", "string"]},
    {"name": "zip", "type": ["null", "string"]},
    {"name": "gender", "type": ["null", "string"]},
    {"name": "email", "type": ["null", "string"]},
    {"name": "username", "type": ["null", "string"]},
    {"name": "password", "type": ["null", "string"]},
    {"name": "phone", "type": ["null", "string"]},
    {"name": "cell", "type": ["null", "string"]},
    {"name": "ssn", "type": ["null", "string"]},
    {"name": "date_of_birth", "type": ["null", "string"]},
    {"name": "reg_date", "type": ["null", "string"]},
    {"name": "large", "type": ["null", "string"]},
    {"name": "medium", "type": ["null", "string"]},
    {"name": "thumbnail", "type": ["null", "string"]},
    {"name": "version", "type": ["null", "string"]},
    {"name": "nationality", "type": ["null", "string"]}
  ]
}

if you have a different schema change it from controller services -> avroRegistrySchema:
![alt text](https://github.com/mohammad-awad-ds/DataEng/blob/main/HomeWork_1/Q1/Guide_Images/B%20Choose%20Schema.PNG)
You can check if your schema is valid by running it on https://json-schema-validator.herokuapp.com/avro.jsp

### I hope you found this useful :)


##### References:
    1. https://community.cloudera.com/t5/Community-Articles/Convert-CSV-to-JSON-Avro-XML-using-ConvertRecord-Apache-NiFi/ta-p/246607
    2. https://www.youtube.com/watch?v=xScWpV_5GQ0&t=51s
    3. https://stackoverflow.com/questions/53417257/how-to-convert-csv-to-json-using-apache-nifi
    

