import numpy as np

np.random.seed(12345)

data1=np.random.rand(3,3)
data2=np.random.randint(0,3)
data3=np.random.randn(3,3)
data4=np.random.normal(size=(3,3))

print('rand:\n',data1)
print('randInt:\n',data2)
print('randn:\n',data3)
print('normal:\n',data4)
