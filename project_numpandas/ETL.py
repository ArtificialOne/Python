#ETL = Extract, Transform, Load (Type of Batch Processing)
#Batch Processing = Multiple sources of information into single source
import glob
import pandas as pd
from datetime import datetime

#####################################EXTRACT#####################################
list_csv=glob.glob('*.csv') #Need CSV files in current folder: Ouptut will be CSV files Composite Functions
list_json=glob.glob('*.json') #Need JSON Files in current folder: Ouptut will be json files Composite Functions

def extract_from_csv(file_to_process): #Extract CSV
    dataframe = pd.read_csv(file_to_process)
    return dataframe

def extract_from_json(file_to_process):#Extract JSON
    dataframe = pd.read_json(file_to_process)
    return dataframe

def extract():
    extracted_data=pd.DataFrame(columns=['Name','Height','Weight']) #Empty data frame to hold extracted data

    for csvfile in glob.glob("*.csv"):#Process all CSV Files
        extracted_data = extracted_data.append(extract_from_csv(csvfile), ignore_index=True)

    for jsonfile in glob.glob("*.json"):
        extracted_data = extracted_data.append(extract_from_json(jsonfile), ignore_index=True)

    return extracted_data


df=extract_from_csv('source1.csv')
df=extract_from_json('source1.json')

#####################################TRANSFORM#####################################

def transform(data):
    data['height'] = round(data.height *0.0254,2) #Convert Height which is in inches to millimeter, 2 decimals
    data['weight'] = round(data.weight * 0.45359237,2) #Convert pounds to kilograms, round 2 decimal places
    return data


#####################################LOAD#####################################

def load(targetfile,data_to_load):
    data_to_load.to_csv(targetfile)

targetfile="transformed_data.csv"

#####################################LOG#####################################

def log(message):
    timestamp_format='%Y-%h-%d-%H:%M:%S'
    now=datetime.now()
    timestamp=now.strftime(timestamp_format)
    with open("logfile.txt",'a') as f:
        f.write(timestamp+','+message+'\n')

#####################################FINALCALL#####################################

log("ETL Job Started")

log("Extracted Phase Started")
extracted_data=extract()
log("Extracted Phase Ended")

log("Transform Job Started")
transformed_data=transform(extracted_data)
log("Transform Job Ended")

log("Load Job Started")
load(targetfile,transformed_data)
log("Load Job Ended")

log("ETL Job Ended")