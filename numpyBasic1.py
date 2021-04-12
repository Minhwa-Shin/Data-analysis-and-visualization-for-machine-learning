import numpy as np

data = [6,7,8,0,1] # List
arr1 = np.array(data) # array
print('data:',data)
print('arr1:',arr1)

data2 = [[1,2,3,4],[5,6,7,8]]
arr2 = np.array(data2)
print('arr2:\n',arr2)

print('ndim:',arr2.ndim)
print('shape:',arr2.shape)
print('dtype:',arr2.dtype)

arr3 = np.array([1,2,3,4,5],dtype=np.float32)
print('arr3 dtype:',arr3.dtype)

arr4 = np.arange(10)
print('arr4:',arr4)

arr5 = np.zeros((3,4))
print('arr5:\n',arr5)

arr6 = np.ones((3,3))
print('arr6:\n',arr6)
