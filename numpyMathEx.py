import numpy as np

arr=np.random.randn(5,4)
print('\n',arr)
print('mean:',arr.mean())
print('mean2:',np.mean(arr));
print('sum:',arr.sum())

print('\n',arr.mean(axis=1))
print('\n',arr.sum(axis=0))

arr=np.array([0,1,2,3,4,5,6,7])
print('\n',arr.cumsum())

arr=np.array([[0,1,2],
             [3,4,5],
             [6,7,8]])
print('\n',arr.cumsum(axis=0))
print('\n',arr.cumprod(axis=1))
