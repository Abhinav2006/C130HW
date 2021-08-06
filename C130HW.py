import pandas as pd
import csv

df = pd.read_csv('totalstars.csv')
print(df.columns)

del df['Star_name.1']
del df['Distance.1']
del df['Mass.1']
del df['Radius.1']
del df['Luminosity']
del df['Unnamed: 6']

df = df.dropna()
df.to_csv("allstars.csv")