import numpy as np

arr=np.empty((8,4))
for i in range(8):
    arr[i]=i

print(arr)
print('\n',arr[[4,3,0,6]])
print('\n',arr[[-3,-5,-7]])

arr=np.arange(8)
arr2=arr.reshape((4,2))
print('\n',arr2)

arr3=arr.reshape((4,2)).reshape(2,4)
print('\n',arr3)


arr4=np.arange(15).reshape((3,5))
print('\n',arr4)
arr5=arr4.T
print('\n',arr5)
