import pandas as pd
import numpy as np

np.random.seed(12345)

rng=pd.date_range('1/1/2019',periods=100,freq='D')
ts=pd.Series(np.random.randn(len(rng)),index=rng)
print(ts,'\n')
print(ts.resample('M'),'\n')
print(ts.resample('M').mean(),'\n')

rng=pd.date_range('1/1/2000',periods=12,freq='T')
ts=pd.Series(np.arange(1,13),index=rng)
print(ts,'\n')
print(ts.resample('5min').sum(),'\n')
print(ts.resample('5min',closed='right').sum(),'\n')
print(ts.resample('5min',closed='right',label='right').sum(),'\n')

print('groupby resampling')
rng=pd.date_range('1/1/2000',periods=100,freq='D')
ts=pd.Series(np.arange(100),index=rng)
print(ts,'\n')
print(ts.groupby(lambda x:x.month).mean(),'\n')
