import numpy as np

arr=np.arange(10)
print('sqrt:\n',np.sqrt(arr))
print('exp:\n',np.exp(arr))

np.random.seed(12345)
x=np.random.randn(8)
y=np.random.randn(8)

print("x:",x)
print("y:",y)
print('maximum:',np.maximum(x,y))
