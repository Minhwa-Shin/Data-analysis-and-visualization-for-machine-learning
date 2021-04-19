import pandas as pd

data=pd.DataFrame({'k1':['one']*3 + ['two']*4,
                   'k2':[1,1,2,3,3,4,4]})
print(data,'\n')
print(data.duplicated(),'\n')
print(data.drop_duplicates(),'\n')

print(data.drop_duplicates(['k1']),'\n')
print(data.drop_duplicates(['k1','k2'],keep='last'),'\n')
