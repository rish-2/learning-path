import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df=pd.read_csv('titanic_data.csv')

x=df['Age']
y=df['Fare']

plt.scatter(x, y)
plt.show()
