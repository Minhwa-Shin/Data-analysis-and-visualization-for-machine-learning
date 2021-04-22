from datetime import datetime
import pandas as pd
import numpy as np
np.random.seed(12345)

dates=[datetime(2017,1,2),datetime(2017,1,5),datetime(2017,1,7),
       datetime(2017,1,8),datetime(2017,1,10),datetime(2017,1,12)]
ts=pd.Series(np.random.randn(6),index=dates)
print(ts,'\n')
print(type(ts),'\n')
print(ts[2],'\n')
print(ts['1/10/2017'],'\n')
print(ts['20170110'],'\n')
print(ts['1/6/2017':'1/11/2017'],'\n')
print(ts.truncate(after='1/9/2017'))
