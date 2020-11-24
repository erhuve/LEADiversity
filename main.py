import csv
import pandas as pd
import plotly.express as px
import plotly.io as pio

newfile = open('cleaned.csv', 'w')
writer = csv.writer(newfile)
writer.writerow(['LEA_NAME','STATE','ZIP','OP'])

df = pd.read_csv('data.csv')

for index, row in df.iterrows():
    writer.writerow([row['LEA_NAME'],row['STATENAME'],row['MZIP'],row['OPERATIONAL_SCHOOLS']])
newfile.close()

# df = pd.read_csv('cleaned.csv')
# leas = df.groupby('STATE')

# print(leas)