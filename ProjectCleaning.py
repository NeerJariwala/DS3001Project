import pandas as pd
import csv
from collections import Counter

data  = pd.read_csv(r"C:\Users\Neer Jariwala\Documents\DS\ChicagoCrimes2.csv")

datetime = data[data.columns[3]]
primetype = data[data.columns[6]]
lat = data[data.columns[20]]
lon = data[data.columns[21]]

d = {'Date / Time' : datetime, 'Primary Type' : primetype, 'Latitude' : lat, 'Longitude' : lon}
df = pd.DataFrame(data=d)
df = df.dropna()
df = df.drop_duplicates()

df['Date / Time'] = pd.to_datetime(df['Date / Time'])

df['Date'] = [d.date() for d in df['Date / Time']]
df['Time'] = [d.time() for d in df['Date / Time']]
df = df.drop(columns = ['Date / Time'])
cols = list(df.columns.values)
cols.pop(cols.index('Date'))
cols.pop(cols.index('Time'))
cols.pop(cols.index('Primary Type'))
cols.pop(cols.index('Latitude'))
cols.pop(cols.index('Longitude'))

df = df[['Date','Time','Primary Type', 'Latitude', 'Longitude']+cols]

df.to_csv("CleanedChicagoData.csv")