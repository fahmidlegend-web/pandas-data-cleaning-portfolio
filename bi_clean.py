import pandas as pd
import numpy as np
import random as rd

df = pd.read_csv("/storage/emulated/0/Documents/CSV Viewer/bi.csv",encoding = 'latin1')

df = pd.read_csv("/storage/emulated/0/Documents/CSV Viewer/bi.csv",encoding = 'latin1')

df["Python"] = pd.to_numeric(df["Python"])
val = df["Python"].mode()
print(val)


df["Python"].loc[df["Python"].isna()] = float(val)
df["gender"] = df["gender"].replace({
"M" : "Male",
"F" : "Female"
})

df["gender"] = df["gender"].str.capitalize()
df["residence"] = df["residence"].str.replace(r'^bi','BI Residence',regex=True, case = False)

df["residence"] = df["residence"].str.replace(r'residence$','',regex=True, case = False)

df["residence"] = df["residence"].str.replace(r'[^a-zA-Z0-9]',' ',regex=True, case = False)

df["prevEducation"] = df["prevEducation"].str.capitalize()

df["prevEducation"].loc[ df["prevEducation"].str.contains(r'chelors$',case=False,na=False)] = "Bachelors"

df["prevEducation"] .loc[df["prevEducation"].str.contains(r'^diplom',case= False,na=False)] = "Diploma"

df["country"] = df["country"].str.capitalize()

changeValues = {
'Norge' : 'Norway',
'Rsa' : 'South Africa',
'Uk' : 'United Kingdom'
}

df["country"] =df["country"].replace(changeValues)

df["entryEXAM"] = pd.to_numeric(df["entryEXAM"])
df["entryEXAM"].loc[df["entryEXAM"] <= 50] = 54


df["fNAME"] = df["fNAME"].str.capitalize()
df["lNAME"] = df["lNAME"].str.capitalize()

df['lNAME'] = df['lNAME'].str.replace('ø','o',regex=True,case=False)

df['fNAME'] = df['fNAME'].str.replace('ø','o',regex=True,case=False)


df["lNAME"] = df["lNAME"].str.normalize('NFKD').str.encode('ascii',errors = 'ignore').str.decode('utf-8')
print(df['fNAME'])

df["DB"] = df["DB"].astype(float)

df["entryEXAM"] = df["entryEXAM"].astype(float)

df.to_csv("/storage/emulated/0/Documents/CSV Viewer/bi_cleaned.csv",index = False)
