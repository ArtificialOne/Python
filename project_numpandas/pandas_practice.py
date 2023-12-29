import pandas as pd
import xml.etree.ElementTree as etree
import asyncio
import json
#https://www.coursera.org/learn/python-for-applied-data-science-ai/ungradedWidget/Pm4xn/cheat-sheet-working-with-data-in-python

#If no headers, pandas will print first row as header. To correct this, use .columns attribute

def download_csv():
    csv_file="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/TopSellingAlbums.csv"
    df=pd.read_csv(csv_file)
    #df.columns=['1st','2nd','Number','Birthday','5','6','7','8','9','10'] #This will create headers
    print(df.head())

    #x=df[['Length']]
    #print(x)

def download_xlsx():
    xlsx_path = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/jupyterlite/files/Module%205/data/TopSellingAlbums.xlsx'
    df=pd.read_excel(xlsx_path)

    x=df[['Length']] #DataFrame
    y=df['Length'] #Series
    z=df[['Artist','Length','Genre']]
    #print(y)
    print(df,'\n')
    #Loc Requires String as Column
    #print(df.iloc[0,0]) #Access index 0 row, index 0 column data point
    #print(df.iloc[1,0]) #Access index 1 row, index 0 column data point
    #print(df.loc[1,'Artist']) #Access location 1 of Arist
    #print(df.iloc[0:2,0:3]) #Splice row 0 up to 2, and column 0 up to 3
    #print(df.loc[0:2,'Artist':'Released']) #Splice location 0 to 2, Arist to Released
    print(f"{df.iloc[0:2]}")

def reading_json():
    with open('filesample.json','r') as openfile: #Open File
        json_object=json.load(openfile) #Read file
    print(json_object) #Print file

def reading_xml(): #Pandas doesn't have an xml attribute, so need to import xml.etree.ElementTree
    tree=etree.parse("fileexample.xml")
    root=tree.getroot()
    columns=["name", "birthday"]
    df=pd.DataFrame(columns=columns)

    for node in root:
        name=node.find("name").text
        birthday=node.find("birthday").text
    df=df.append(pd.Series([name,birthday], index=columns), ignore_index=True) #Append data to data frame

download_csv()
#download_xlsx()