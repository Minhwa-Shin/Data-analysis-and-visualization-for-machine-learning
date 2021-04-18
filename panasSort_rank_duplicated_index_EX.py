import pandas as pd
import numpy as np

# sort
obj=pd.Series(range(4),index=list('dabc'))
print('\n',obj)
print('\n',obj.sort_index())

frame=pd.DataFrame(np.arange(8).reshape(2,4),index=['three','one'],columns=list('dabc'))
print('\n',frame)
print('\n',frame.sort_index())
print('\n',frame.sort_index(axis=1))
print('\n',frame.sort_index(axis=1,ascending=False))

obj=pd.Series([4,8,-2,1])
print('\n',obj.sort_values())

frame=pd.DataFrame({'b':[4,7,-3,2],'a':[0,1,0,1]})
print('\n',frame)
print('\n',frame.sort_values(by=['a','b']))

# rank
obj=pd.Series([7,-5,7,4,2,0,4])
print('\n',obj.rank())

# duplicated index
obj=pd.Series(range(5),index=['a','a','b','b','c'])
print('\n',obj)
print(obj.index.is_unique,'\n')
print(obj['a'],'\n')

df=pd.DataFrame(np.random.randn(4,3),index=['a','a','b','b'])
print(df,'\n')
print(df.loc['b'],'\n')
