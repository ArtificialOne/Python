from typing import List
import pandas as pd
from datetime import datetime

TARGET_FILE = 'transformed_data.csv'

def extract_from_csv(file_path: str) -> pd.DataFrame:
  try:
    df = pd.read_csv(file_path)  
  except Exception as e:
    print(f'Failed to parse {file_path}')
    raise e

  return df

# Similarly add types and validation for other functions

class ETL:

  def __init__(self):
    self.extracted_df = pd.DataFrame()

  def extract(self) -> None:
    '''Extract data from all csv and json files'''
    pass

  def transform(self) -> None:
    '''Transform extracted data'''
    pass
  
  def load(self, df: pd.DataFrame) -> None:
    '''Save transformed data to target CSV'''
    pass

  def log(self, msg: str) -> None:
    '''Simple logger to file'''
    pass

  def run(self) -> None:
    '''Orchestrate ETL process'''
    self.extract()
    self.transform()
    self.load(self.extracted_df)

if __name__ == '__main__':
  etl = ETL()
  etl.run()