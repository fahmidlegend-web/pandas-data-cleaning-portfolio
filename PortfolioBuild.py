import pandas as pd
import csv
import re
import random
import string
objDf = pd.read_csv("/storage/emulated/0/Documents/CSV Viewer/portfolio_sample.csv")

#Id formatting:
numbers = objDf["Id"].str.extract(r'(\d+)')
objDf["Id"] = "C_" + numbers[0].str.zfill(3)

#Filling missing data in ID column:
fillValue = {27 : "C_027",28: "C_028",29:"C_029",30:"C_030"}
objDf["Id"]= objDf["Id"].fillna(fillValue)
#print(objDf["Id"].loc[objDf["Id"].isna()])
#print(objDf["Id"].iloc[27:33])
#print(objDf["Id"].unique())
nameList = ["Mahir","Farhan","Rahim","Ahad","Tuad","Maliha","Fariha","Kumar","Mahir","Farjad"]

objDf["Name"].loc[objDf["Name"].isna()] = random.choices(nameList,k= objDf["Name"].isna().sum())

objDf["Name"].loc[objDf["Name"] == "ERROR"] = random.choices(nameList,k=3)
#print(objDf["Name"].loc[objDf["Name"] == "ERROR"])

numbers = random.choices(string.digits,k=4)
phoneNum = "+89" + "".join(numbers)
print(phoneNum)


val = random.choices(string.digits,k= random.randint(3,6))
Values = "" .join(val)

objDf["phone"].loc[objDf["phone"].isna()] = phoneNum
objDf["phone"].loc[objDf["phone"] == "ERROR"] = phoneNum
objDf["phone"].loc[objDf["phone"] == "127"] = phoneNum
objDf["phone"].loc[objDf["phone"] == "3339"] = phoneNum


objDf["phone"].loc[objDf["phone"].isna()] = phoneNum


objDf["Order"].loc[objDf["Order"] == "ERROR"] = Values
objDf["Name"] = objDf["Name"].str.strip().str.title()

objDf["Order"] = objDf["Order"].str.replace(r'\$','',regex = True)

objDf["Order"] = pd.to_numeric(objDf["Order"], errors='coerce')
objDf["Order"].loc[objDf["Order"].isna()] = Values
print(objDf["Order"].dtype)
#print("No of Missing data:",objDf["Name"].isna().sum())

#print(objDf["Name"].isna().sum())
#print(numbers)

#objDf = objDf.apply(lambda row: ",".join(row.dropna().astype(str)), axis=1).str.split(",", expand=True)

#print(objDf.columns)
#print(objDf.iloc[0])

#print(objDf.iloc[0:-3])

#objDf["Order"] = objDf["Order"].str.replace(" ",",")


#objDf["Order"] = objDf["order"].fillna(",").astype(str) + "" + 
#for i, col in enumerate(objDf.colu.mns):
    #print(i, repr(col))
#suspectedCol = objDf.columns[objDf.isna().mean() > 0.8]
#print(suspectedCol
    

#objDf = objDf.drop(columns=["Email","Column1","Column2"]
#
objDf.to_csv("/storage/emulated/0/Documents/CSV Viewer/portfolio_sample3.csv",index = False,quoting=csv.QUOTE_ALL)