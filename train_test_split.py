import pandas as pd
import numpy as np 
from sklearn.model_selection import train_test_split

data = pd.read_csv('AmesHousing_clean.csv')

y = data.SalePrice

X = data.drop(['SalePrice', 'Order', 'PID'], axis = 1)

train_X, test_X, train_y, test_y = train_test_split(X,y, test_size=0.20)

train_X.to_csv("train_X", index=False)
test_X.to_csv("test_X", index = False)
train_y.to_csv("train_y", index = False)
test_y.to_csv("test_y", index = False)