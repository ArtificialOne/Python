import glob
import pandas as pd
import xml.etree.ElementTree as ET
from datetime import datetime

logfile    = "logfile.txt"
targetfile = "transformed_data.csv"

def extract_from_csv(file_to_process):
    dataframe = pd.read_csv(file_to_process)
    return dataframe

def extract_from_json(file_to_process):
    dataframe = pd.read_json(file_to_process,lines=True)
    return dataframe

def extract_from_xml(file_to_process):
    data_list=[]
    tree = ET.parse(file_to_process)
    root = tree.getroot()
    for person in root:
        name = person.find("name").text
        height = float(person.find("height").text)
        weight = float(person.find("weight").text)
        data_list.append({"name":name, "height":height, "weight":weight})
    dataframe=pd.concat([pd.DataFrame(data_list)],ignore_index=True)
    return dataframe

def extract():
    extracted_data = pd.DataFrame(columns=['name','height','weight']) # create an empty data frame to hold extracted data

    for csvfile in glob.glob("*.csv"):
        df=extract_from_csv(csvfile)
        extracted_data = pd.concat([extracted_data,df], ignore_index=True)
        
    for jsonfile in glob.glob("*.json"):
        df=extract_from_json(jsonfile)
        extracted_data = pd.concat([extracted_data,df], ignore_index=True)

    for xmlfile in glob.glob("*.xml"):
        df=extract_from_xml(xmlfile)
        extracted_data = pd.concat([extracted_data,df], ignore_index=True)
        
    return extracted_data

def transform(data):
    data['height'] = round(data.height * 0.0254,2)
    data['weight'] = round(data.weight * 0.45359237,2)
    return data

def load(targetfile,data_to_load):
    data_to_load.to_csv(targetfile)

def log(message):
    timestamp_format = '%Y-%h-%d-%H:%M:%S' # Year-Monthname-Day-Hour-Minute-Second
    now = datetime.now() # get current timestamp
    timestamp = now.strftime(timestamp_format)
    with open("logfile.txt","a") as f:
        f.write(timestamp + ',' + message + '\n')

log("ETL Job Started")

log("Extract phase Started")
extracted_data = extract()
log("Extract phase Ended")
extracted_data

log("Transform phase Started")
transformed_data = transform(extracted_data)
log("Transform phase Ended")
transformed_data 

log("Load phase Started")
load(targetfile,transformed_data)
log("Load phase Ended")

log("ETL Job Ended")