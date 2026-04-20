import pandas as pd
import numpy as np
import random as rd

df = pd.read_csv("/storage/emulated/0/Documents/CSV Viewer/bi.csv",encoding = 'latin1')



df.to_csv("/storage/emulated/0/Documents/CSV Viewer/bi_cleaned.csv",index = False)