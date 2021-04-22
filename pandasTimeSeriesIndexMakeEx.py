import pandas as pd
import numpy as np
np.random.seed(12345)

index=pd.date_range('4/1/2012','6/1/2012')
print(index,'\n')
print(pd.date_range(start='4/1/2012',periods=20),'\n')
print(pd.date_range(end='6/1/2012',periods=20),'\n')

from pandas.tseries.offsets import Hour, Minute
hour=Hour()
print(hour,'\n')
four_hour=Hour(4)
print(four_hour,'\n')
print(pd.date_range('1/1/2018','1/3/2018 23:59',freq='4h'),'\n')
print(pd.date_range('1/1/2018',periods=10,freq='1h30min'),'\n')

rng=pd.date_range('1/1/2019','9/1/2019',freq='WOM-2FRI')
print(rng,'\n')
print(list(rng),'\n')
