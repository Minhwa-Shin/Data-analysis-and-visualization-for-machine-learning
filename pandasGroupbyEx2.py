import pandas as pd
import numpy as np
np.random.seed(12345)

df=pd.DataFrame({'key1':['a','a','b','b','a'],
                 'key2':['one','two','one','two','one'],
                 'data1':np.random.randn(5),
                 'data2':np.random.randn(5)})
print(df,'\n')

grouped=df['data1'].groupby(df['key1'])
print(grouped,'\n')
print(grouped.mean(),'\n')

means=df['data1'].groupby([df['key1'],df['key2']]).mean()
print(means,'\n')

for name,group in df.groupby(df['key1']):
    print('name:',name)
    print(group,'\n')
