import pandas as pd 
import numpy as np 

df = pd.read_csv('houseData.csv')

print(df['Exterior Features:'].unique())
print(len(df['Exterior Features:'].unique()))