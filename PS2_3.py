import pandas as pd
import math
import matplotlib.pyplot as plt

temp=pd.read_csv('C:\\Users\\王野\\Desktop\\编程课\\PS2\\99405099999.csv')
###3.1clean missing values
temp['temperature']=temp['TEMP'].dropna()
#print(temp['temperature'])

###3.2Plot the time series
#temp['temperature'].plot()
#plt.show()

###3.3 5 simple statistical checks
print(temp['temperature'].count())
print(temp['temperature'].mean())
print(temp['temperature'].max())
print(temp['temperature'].min())
temp['dy']=pd.to_datetime(temp['DATE'])
temp['month']=temp['dy'].astype("str").str[5:7]
temp.groupby(['month'])['temperature'].mean().plot()
plt.show()