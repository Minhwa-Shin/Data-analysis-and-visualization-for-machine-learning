import pandas as pd
import numpy as np

df1 = pd.DataFrame(np.arange(12).reshape(3,4),columns=['a','b','c','d'])
df2 = pd.DataFrame(np.arange(20).reshape(4,5),columns=['a','b','c','d','e'])

print(df1)
print('')
print(df2)
print('')
print(df1+df2)
print('')
print(df1.add(df2,fill_value=0))

frame=pd.DataFrame(np.arange(12).reshape(4,3),index=['Utah','Ohio','Texas','Oregon'],columns=list('bde'))
print(frame)

# series=frame.loc['Utah']
# print(series,type(series))
series=frame.iloc[0]
print(series,type(series))

print(frame-series)
