import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (12.0, 9.0)

# Preprocessing Input data
data = pd.read_csv('laptop_price - dataset.csv')
X = data.iloc[:, 0]
Y = data.iloc[:, 1]
#plt.scatter(X, Y)
#plt.show()
print(data.head())
print(data["Company"].unique())
