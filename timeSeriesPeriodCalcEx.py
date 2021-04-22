import pandas as pd

p=pd.Period(2010,freq='A-DEC')
print(p,'\n')
print(p+5,'\n')
print(p-2,'\n')
print(pd.Period('2017',freq='A-DEC')-p,'\n')
