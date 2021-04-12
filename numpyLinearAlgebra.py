import numpy as np

x=np.array([[1,2,3],[4,5,6]])
y=np.array([[6,23],[1,-7],[8,9]])
print(x.dot(y))

print('\n',np.dot(x,np.ones(3)))

from numpy.linalg import inv,qr
x2=np.random.randn(5,5)
mat=x2.T.dot(x2)
print('\n',inv(mat))

q,r=qr(mat)
print('q:\n',q)
print('r:\n',r)

data=np.identity(6)
print('\n',data)
