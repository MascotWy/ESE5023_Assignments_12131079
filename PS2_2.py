import pandas as pd
import matplotlib.pyplot as plt

wind=pd.read_csv('C:\\Users\\王野\\Desktop\\编程课\\PS2\\2281305.csv')
wind['month']=wind['DATE'].astype("str").str[0:7]
wind['speed']=wind['WND'].str[8:12].astype("float")
wind.groupby(['month'])['speed'].mean().plot()
plt.show()
#print(wind['month'])
#print(wind['speed'])