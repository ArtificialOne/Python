import matplotlib.pyplot as plt
import pandas as pd
import pylab as pl
import numpy as np

path="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ML0101EN-SkillsNetwork/labs/Module%202/data/FuelConsumptionCo2.csv"
file="FuelConsumption.csv"

async def download(url, filename):
    response = await (url)
    if response.status == 200:
        with open(filename, "wb") as f:
            f.write(await response.bytes())

    await download(path, "FuelConsumption.csv")
    path="FuelConsumption.csv"

    df = pd.read_csv("FuelConsumption.csv")
    print(df.head())

download(path,file)