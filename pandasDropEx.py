import pandas as pd
import numpy as np

obj=pd.Series(np.arange(4.),index=['a','b','c','d'])
print(obj)
print('\n',obj['b'])
print('\n',obj[1])
print('\n',obj[2:4])
print('\n',obj[[1,3]])
print('\n',obj[obj<2])
print('\n',obj['b':'c'])
print('\n',obj['b':'d'])

obj=pd.Series(np.arange(5.),index=['a','b','c','d','e'])
print('\n',obj)

newobj=obj.drop('c')
print('\n',newobj)
print('\n',obj.drop(['d','c']))

data=pd.DataFrame(np.arange(16).reshape((4,4)),
                  index=['Ohio','Colorado','Utah','New York'],
                  columns=['one','two','three','four'])
print('\n',data)
print('\n',data.drop(['Colorado','Ohio']))
print('\n',data.drop(columns=['two','four']))
