import pandas as pd

s1=pd.Series([0,1],index=['a','b'])
s2=pd.Series([2,3,4],index=['c','d','e'])
s3=pd.Series([5,6],index=['f','g'])

print(pd.concat([s1,s2,s3],axis=0),"\n")
print(pd.concat([s1,s2,s3],axis=1),"\n")
