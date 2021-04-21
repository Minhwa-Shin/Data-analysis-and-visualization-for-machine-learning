import pandas as pd

tips=pd.read_csv('tips.csv')
tips['tip_pct']=tips['tip']/tips['total_bill']

# print(tips.groupby(['sex','smoker']).sum(),'n')
print(tips.pivot_table(index=['sex','smoker']),'\n')
print(tips.pivot_table(['tip_pct','size'],
                       index=['sex','day'],
                       columns='smoker'),'\n')

print(tips.pivot_table('tip_pct',
                       index=['sex','day'],
                       columns='smoker',
                       aggfunc=len),'\n')
