import pandas as pd

df1=pd.DataFrame({'key':['b','b','a','c','a','a','b'],'data1':range(7)})
df2=pd.DataFrame({'key':['a','b','d'],'data2':range(3)})

print(df1,"\n")
print(df2,"\n")
print(pd.merge(df1,df2),"\n")
print(pd.merge(df1,df2,on='key'),"\n")

print("how\n")
print(pd.merge(df1,df2,how='outer'),"\n")
print(pd.merge(df1,df2,how='left'),"\n")
print(pd.merge(df1,df2,how='right'),"\n")
print(pd.merge(df1,df2,how='inner'),"\n")

df3=pd.DataFrame({'lkey':['b','b','a','c','a','a','b'],'data1':range(7)})
df4=pd.DataFrame({'rkey':['a','b','d'],'data2':range(3)})
print(pd.merge(df3,df4,left_on='lkey',right_on='rkey'),"\n")
