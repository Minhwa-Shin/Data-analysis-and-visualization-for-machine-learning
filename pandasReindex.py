import pandas as pd

obj=pd.Series([4.5,7.2,-5.3,3.6],index=['d','b','a','c'])
print('\n',obj)

obj2=obj.reindex(['a','b','c','d','e'])
print('\n',obj2)

obj3=pd.Series(['blue','yellow','purple'],index=[0,2,4])
print('\n',obj3)

obj4=obj3.reindex(range(6),method='ffill')
print('\n',obj4)
