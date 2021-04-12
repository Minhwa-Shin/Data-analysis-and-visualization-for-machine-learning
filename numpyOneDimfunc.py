import numpy as np

arr=np.random.randn(3,3)
print('\n',arr)

arr.sort(axis=1)
print('\n',arr)

arr.sort(axis=0)
print('\n',arr)

intData=np.array([3,3,3,2,2,1,1,4,4])
print('uniquqe:',np.unique(intData))

values=np.array([6,0,0,3,2,5,6])
print('union:',np.union1d(values,[2,3,6]))
print('intersection:',np.intersect1d(values,[2,3,6]))
print('difference:',np.setdiff1d(values,[2,3,6]))
