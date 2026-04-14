import pandas as pd
import numpy as np

df =  pd.read_csv("/storage/emulated/0/Documents/CSV Viewer/Portfolio_2.csv",encoding = 'latin1')

df.drop(columns = ["Column1","Column2"])

print(df)

#df. to_csv("/storage/emulated/0/Documents/CSV Viewer/Portfolio_2.csv",encoding = 'latin1')