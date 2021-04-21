import pandas as pd
import numpy as np

states=['Ohio','New York','Vermont','Florida',
        'Oregon','Nevada','California','Idaho']
group_key=['East']*4+['West']*4
data=pd.Series(np.random.randn(8),index=states)
data[['Vermont','Nevada','Idaho']]=np.nan
print(data,'\n')

fill_mean=lambda g: g.fillna(g.mean())
print(data.groupby(group_key).apply(fill_mean),'\n')

fill_values={'East':0.5,'West':-1}
fill_func=lambda g: g.fillna(fill_values[g.name])
print(data.groupby(group_key).apply(fill_func),'\n')
