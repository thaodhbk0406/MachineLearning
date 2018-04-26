import json
import pandas as pd 

with open('train.json') as json_data:
    d = json.load(json_data)
df=pd.DataFrame(d)
df2=(df['sentiment'])
print(df2.head())