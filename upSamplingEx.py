import pandas as pd
import numpy as np

frame=pd.DataFrame(np.random.randn(2,4),
                   index=pd.date_range('1/1/2000',periods=2,freq='W-WED'),
                   columns=['Colorado','Texas','New York','Ohio'])

print(frame,'\n')
print(frame.resample('D').ffill(),'\n')
print(frame.resample('D').ffill(limit=2),'\n')
print(frame.resample('W-FRI').ffill(),'\n')

frame=pd.DataFrame(np.random.randn(24,4),
                   index=pd.period_range('1-2000','12-2001',freq='M'),
                   columns=['Colorado','Texas','New York','ohio'])
print(frame,'\n')
annual_frame=frame.resample('A-DEC').mean()
print(annual_frame,'\n')
print(annual_frame.resample('Q-DEC').ffill(),'\n')
