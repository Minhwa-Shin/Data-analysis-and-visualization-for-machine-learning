import pandas as pd
import numpy as np

data=pd.Series([1.,-999.,2.,-1000.,3.])
print(data,'\n')
print(data.replace([-999,-1000],np.nan),'\n')
print(data.replace({-999:np.nan,-1000:0}),'\n')
