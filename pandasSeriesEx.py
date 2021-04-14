import pandas as pd
import numpy as np

obj=pd.Series([4,7,-5,3])

print('\n',obj)
print('\n',obj.values)
print('\n',obj.index)

obj2=pd.Series([4,7,-5,3],index=['d','b','a','c'])
print('\n',obj2)

print(obj2>0)
print(obj2[obj2>0])
print('\n',obj2*2)
print('\n',np.exp(obj2))
