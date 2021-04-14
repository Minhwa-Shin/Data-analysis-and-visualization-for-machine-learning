import numpy as np
import pandas as pd

data={'state':['Ohio','Ohio','Ohio','Nevada','Nevada','Nevada'],
      'year':[2000,2001,2002,2001,2002,2003],
      'pop':[1.5,1.7,3.6,2.4,2.9,3.2]}

frame=pd.DataFrame(data)

print('\n',frame)
print(type(frame))

print(frame['state'])
print(frame.state)
print(frame.loc[0])

frame=pd.DataFrame(data,columns=['year','state','pop','debt'],
                   index=['0ne','two','three','four','five','six'])
print('\n',frame) #NaN : Not a Number == null
print('\n',frame.columns)
print('\n',frame['state'])
print('\n',frame.year)
print('\n',frame.loc['two'])

frame['debt']=20
print('\n',frame)
frame['debt']=[10,20,30,40,50,60]
print('\n',frame)
