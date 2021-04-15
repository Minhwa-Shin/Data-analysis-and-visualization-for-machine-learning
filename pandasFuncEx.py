import pandas as pd
import numpy as np

frame=pd.DataFrame(np.random.randn(4,3),columns=list('bde'),index=['Utah','Ohio','Texax','Oregon'])
print('\n',frame)
print('\n',np.abs(frame))

lambda_Func=lambda x : x.max()-x.min()
print('\n',frame.apply(lambda_Func))
print('\n',frame.apply(lambda_Func,axis=1))

def Func1(x):
    return pd.Series([x.min(),x.max()],index=['minV','maxV'])
print('\n',frame.apply(Func1))
print('\n',frame.apply(Func1,axis=1))
