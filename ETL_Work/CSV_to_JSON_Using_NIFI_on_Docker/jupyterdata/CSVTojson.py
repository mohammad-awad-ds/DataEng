try: 
    import pandas as pd
    import sys
except:
    $pip install pandas
    $pip install sys
    import pandas as pd
    import sys

df=pd.read_csv('data.csv')
df=df[['name']]
print(df.head())
df.to_json('/opt/nifi/database_repository/dataJSON.json', orient='records')

