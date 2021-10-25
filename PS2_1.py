import pandas as pd
import matplotlib.pyplot as plt
earthquakes=pd.read_csv('C:\\Users\\王野\\Desktop\\编程课\\PS2\\earthquakes-2021-10-22_10-51-46_+0800.tsv',sep='\t')
###1.1 top ten countries along with the total number of deaths
#earthquakes.groupby('Country').sum()['Total Injuries'].head(10)

###1.2 time series of total number of earthquakes with magnitude larger than 6.0
# count=earthquakes[earthquakes['Mag']>6]['Year'].value_counts()
# count.plot()
# plt.show()

###1.3
def CountEq_LargestEq(string):
    CountEq2=len(earthquakes[earthquakes['Countries']==string]['Year'].value_counts())
    LargestEq_index=earthquakes[earthquakes['Countries']==string]['magnitude'].idxmax()
    LargestEq2 = str(int(earthquakes.loc[LargestEq_index-1]['Yr']))+'-'+str(int(earthquakes.loc[LargestEq_index-1]['Month']))+'-'+str(int(earthquakes.loc[LargestEq_index-1]['Day']))
    return CountEq2,LargestEq2

Countries=[]
CountEqList=[]
LargestEqList=[]
earthquakes['Yr']=earthquakes['Year'].fillna(value=0)
earthquakes['Month']=earthquakes['Mo'].fillna(value=0)
earthquakes['Day']=earthquakes['Dy'].fillna(value=0)
earthquakes['Countries']=earthquakes['Country'].fillna(value='Others')
earthquakes['magnitude']=earthquakes['Mag'].fillna(value=0)

for i in earthquakes['Countries'].drop_duplicates().dropna().values:
    Countries.append(i)
    CountEq,LargestEq=CountEq_LargestEq(i)
    CountEqList.append(CountEq)
    LargestEqList.append(LargestEq)
diction=dict(zip(Countries,CountEqList))
print(sorted(diction.items(),key=lambda x:x[1],reverse=True))

