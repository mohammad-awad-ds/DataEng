# Q1 NIFI
The purpose of this excercise is to convert CSV files into JSON.
## Beginning
```sh
$ docker-compose up
```

## Connections
Connect to jupyter with localhost:8888
Connect to Nifi using localhost:8080

## Tutorial on how to set up NIFI workflow 
https://www.youtube.com/watch?v=xScWpV_5GQ0&t=58s

## Generate Data: 
Using faker to generate data. Just run the create_data notebook.

![image](https://github.com/mohammad-awad-ds/DataEng/blob/main/Images/Create%20directory%20files%20required.PNG)

## Drop a get file processor to feed in the CSV file
![image](https://github.com/mohammad-awad-ds/DataEng/blob/main/Images/1getfile%20pref.PNG)

## Use a record converter with the following setup

![image](https://github.com/mohammad-awad-ds/DataEng/blob/main/Images/CVS%20record%20writer.PNG

## Enable Services 
![image](https://github.com/mohammad-awad-ds/DataEng/blob/main/Images/5Controller%20Services.PNG)

You can get avroschema from https://toolslick.com/generation/metadata/avro-schema-from-json by feeding the JSON file schema you want.

The following was generated from the tool.
```
{
  "name": "MyClass",
  "type": "record",
  "namespace": "com.acme.avro",
  "fields": [
    {
      "name": "name",
      "type": "string"
    },
    {
      "name": "age",
      "type": "int"
    }
  ]
}
```


## Run Work flow from the left hand side panel in Nifi

## Final Template
![image](https://github.com/mohammad-awad-ds/DataEng/blob/main/Images/template.PNG)



