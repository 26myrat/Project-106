import csv
import plotly.express as px
import pandas as pd
import numpy as np 
df=pd.read_csv("Student Marks vs Days Present.csv")
fig= px.scatter(df,x="Marks In Percentage", y="Days Present")
fig.show()
def findCorelation(datasource):
    corelation= np.corrcoef(datasource["x"], datasource["y"])
    print("Corelation between the student's grades and their attendance:", corelation[0,1])

def getDataSource(dataPath):
    studentMarks= []
    daysPresent= []
    with open(dataPath)as f:
        csvReader= csv.DictReader(f)
        for row in csvReader:
            studentMarks.append(float(row["Marks In Percentage"]))
            daysPresent.append(float(row["Days Present"]))
    return{"x":studentMarks, "y": daysPresent}

def setup():
    dataPath= "Student Marks vs Days Present.csv"
    dataSource= getDataSource(dataPath)
    findCorelation(dataSource)
setup()