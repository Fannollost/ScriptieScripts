import pandas as pd
import csv
import numpy as np

df = pd.read_csv("lsc22_metadata.csv")
omitted = 0
for index, row in df.iterrows():
    lat = row["latitude"]
    if(np.isnan(lat)):
        omitted +=1

print(omitted)