import pandas as pd

df=pd.read_csv('ex1.csv')
print(df,'\n')

print(pd.read_csv('ex2.csv',header=None))
print(pd.read_csv('ex2.csv',names=['one','two','three','four','message']),'\n')
print(pd.read_csv('ex2.csv',names=['one','two','three','four','message'],index_col='four'),'\n')
print(pd.read_csv('ex4.csv',skiprows=[0,2,3]),'\n')
