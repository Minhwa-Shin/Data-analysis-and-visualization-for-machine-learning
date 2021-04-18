import numpy as np
import pandas as pd

df=pd.DataFrame([[1.40,np.nan],[7.10,-4.5],[np.nan,np.nan],[0.75,-1.3]],index=['a','b','c','d'],columns=['one','two'])
print(df,'\n')
print(df.sum(),'\n')
print(df.sum(axis=1),'\n')
print(df.describe(),'\n')

price=pd.read_pickle('yahoo_price.pkl')
volume=pd.read_pickle('yahoo_volume.pkl')

print(price,'\n')
print(volume,'\n')

pdata=price.pct_change()
print(pdata.tail(),'\n')
print(pdata.MSFT.corr(pdata.IBM),'\n')
print(pdata.MSFT.cov(pdata.IBM),'\n')
print(pdata.corr(),'\n')
print(pdata.cov(),'\n')
print(pdata.corrwith(pdata.IBM),'\n')
