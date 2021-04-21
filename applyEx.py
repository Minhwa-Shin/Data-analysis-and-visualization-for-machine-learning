import pandas as pd

tips=pd.read_csv('tips.csv')
tips['tip_pct']=tips['tip'] / tips['total_bill']

def top(df,n=5,column='tip_pct'):
    return df.sort_values(by=column)[-n:]

# print(tips.groupby(['smoker','day']).apply(top),'\n')
print(tips.groupby(['smoker','day']).apply(top,n=1,column='total_bill'),'\n')
