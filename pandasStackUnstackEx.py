import pandas as pd
import numpy as np

data=pd.DataFrame(np.arange(6).reshape(2,3),
                  index=pd.Index(['Ohoio','Colorado'],name='state'),
                  columns=pd.Index(['one','two','three'],name='number'))
print(data,'\n')
result=data.stack()
print(result,'\n')
print(result.unstack(),'\n')

print(result.unstack(level=0),'\n')
print(result.unstack(level=1),'\n')
print(result.unstack('state'),'\n')
print(result.unstack('number'),'\n')

print('\n\nconcat unstack')
s1=pd.Series([0,1,2,3],index=['a','b','c','d'])
s2=pd.Series([4,5,6],index=['c','d','e'])
data2=pd.concat([s1,s2],keys=['one','two'])
print(data2,'\n')
print(data2.unstack(level=0),'\n')
