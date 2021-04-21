import pandas as pd
import numpy as np

tips=pd.read_csv('tips.csv')
tips['tip_pct']=tips['tip']/tips['total_bill']
print(tips,'\n')

grouped=tips.groupby(['sex','smoker'])
grouped_pct=grouped['tip_pct']

print(grouped_pct.agg('mean'),'\n')
print(grouped_pct.agg(['mean','std']),'\n')
print(grouped_pct.agg([('average','mean'),('standard deviation','std')]),'\n')
print(grouped.agg({'tip_pct':['min','max','std'],
                   'size':['sum','mean']}),'\n')
