import pandas as pd

ages=[20,22,25,27,21,23,37,31,61,45,41,32]
bins=[18,25,35,60,100]
cuts=pd.cut(ages,bins)
print(cuts,'\n')
print(pd.cut(ages,bins,right=False),'\n')
print(pd.value_counts(cuts),'\n')

group_name=['Youth','YoungAdult','MiddleAged','Senior']
rnData=pd.cut(ages,bins,labels=group_name)
print(rnData,'\n')
print(pd.value_counts(rnData),'\n')
