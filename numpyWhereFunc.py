import numpy as np

xarr=np.array([1.1,1.2,1.3,1.4,1.5])
yarr=np.array([2.1,2.2,2.3,2.4,2.5])
cond=np.array([True,False,True,True,False])

#print(list(zip(xarr,yarr,cond)))
result=[(x if c else y) for x,y,c in zip(xarr,yarr,cond)]
print('result:',result)

result2=np.where(cond,xarr,yarr)
print('result2:',result2)

print(type(result),type(result2))

np.random.seed(12345)
arr=np.random.randn(4,4)
print('arr:\n',arr)
print(np.where(arr>0,2,-2))
print(np.where(arr>0,2,arr))
