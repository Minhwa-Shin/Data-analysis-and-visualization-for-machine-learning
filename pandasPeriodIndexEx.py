import pandas as pd

data=pd.read_csv('macrodata.csv')
print(data,'\n')

index=pd.PeriodIndex(year=data.year,quarter=data.quarter,freq='Q-DEC')
data.index=index
print(data,'\n')
