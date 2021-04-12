import numpy as np

arr=np.random.randn(100)
print('\n',(arr>0).sum(),'\n')

bools=np.array(([[False,False,True,False],
                 [False,False,False,False]]))
print(bools.any(axis=1),'\n')
print(bools.all(axis=0),'\n')

data=np.random.randn(10,4)
data=data*2
print('\ndata:\n',data)
print('\ndata[(data>3).any(axis=1)]:\n',data[(data>3).any(axis=1)])

arr=np.random.randn(5,3)
print('\n',arr)
