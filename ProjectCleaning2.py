import pandas as pd
import csv
from collections import Counter


df = pd.read_csv(r"C:\Users\Neer Jariwala\.spyder-py3\CleanedChicagoData.csv")

counted = []

sorted_data = df.sort_values(by = 'Primary Type')
counted = Counter(sorted_data[sorted_data.columns[2]])
dfcalc = pd.DataFrame.from_dict(counted, orient='index').reset_index()


dfmean = dfcalc[0].mean()
dfmedian = dfcalc[0].median()
dfmode = dfcalc[0].mode()