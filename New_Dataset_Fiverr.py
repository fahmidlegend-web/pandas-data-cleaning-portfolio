import pandas as pd
import re
import random

df = pd.read_csv("/storage/emulated/0/Documents/CSV Viewer/New_Dataset_Fiverr.csv")
df = df.dropna("Column 1")
