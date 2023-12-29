import pandas as pd

def file_read():
    csv_path="C:\\Users\\Artificial\\Documents\\xxPython\\projects\\MLKaggle\\Lottery_Powerball_Winning_Numbers__Beginning_2010.csv"
    df= pd.read_csv(csv_path)
    print(f"HEADES: \n {df.head()}\n")
    print(f"DESCRIPTION: \n{df.describe()}\n")
    print(f"DATA INFO:\n {df.info()}\n")

file_read()