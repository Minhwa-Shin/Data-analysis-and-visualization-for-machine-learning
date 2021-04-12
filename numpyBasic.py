import numpy as np

arr=np.array([[1,2,3],[4,5,6]])
print('arr:\n',arr)

print('arr*arr:\n',arr*arr)
print('arr-arr:\n',arr-arr)
print('1/arr\n:',1/arr)
print('arr**0.5:\n',arr**0.5)

arr2=np.arange(10)
print("\n",arr2[5])
print("\n",arr2[5:8])
arr2[5:8]=12
print("\n",arr2)

arr3=np.array([[1,2,3],[4,5,6],[7,8,9]])
print('\n',arr[:2])
print('\n',arr[:2,1:])

np.random.seed(12345)
names=np.array(['Bob','Joe','Will','Bob','will','Joe','Joe'])
data=np.random.rand(7,4);
print('\n',names,'\n')
print('\n',data)

print('\n',names=='Bob')
print('\n',data[names=='Bob'])

print('\n',data[names=='Bob',2:])
print('\n',data[names=='Bob',3])
