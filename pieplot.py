import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df=pd.read_csv('titanic_data.csv')

m=df.loc[df['Sex']=='male'].count()[0]
f=df.loc[df['Sex']=='female'].count()[0]
l=["Male Passengers","Female Passengers"]
col=["#aaabca","#abcaac"]
plt.pie([m,f],labels=l,colors=col,shadow=True,explode=[0.2,0])
plt.show()

        
         
        