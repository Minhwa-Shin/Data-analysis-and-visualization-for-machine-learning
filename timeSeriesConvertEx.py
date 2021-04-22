import pandas as pd
import numpy as np

rng=pd.date_range('1/1/2019',periods=3,freq='M')
print(rng,'\n')

ts=pd.Series(np.random.randn(3),index=rng)
print(ts,'\n')

pts=ts.to_period('M')
print(pts,'\n')

print(pts.to_timestamp(how='end'))
