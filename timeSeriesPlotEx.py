import pandas as pd
import matplotlib.pyplot as plt

close_px_all=pd.read_csv('stock_px.csv',parse_dates=True,index_col=0)
close_px=close_px_all[['AAPL','MSFT','XOM']]
close_px=close_px.resample('B').ffill()
print(close_px.info(),'\n')
print(close_px.head(10),'\n')

close_px['AAPL'].plot()
plt.show()

close_px['AAPL'].loc['01-2011':'03-2011'].plot()
plt.show()
