try: 
    import pandas as pd
except:
    !pip install pandas
    import pandas as pd


def CSVToJson():
    df=pd.read_csv('data.csv') 
    for i,r in df.iterrows():
        print(r['name'])
    
    df.to_json('fromNifi.json', orient= 'records')