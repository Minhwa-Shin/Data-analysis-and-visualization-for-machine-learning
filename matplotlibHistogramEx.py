import numpy as np
import matplotlib.pyplot as plt

mu1,mu2,sigma=100,130,15
x1=mu1+sigma*np.random.randn(10000)
x2=mu2+sigma*np.random.randn(10000)

fig=plt.figure()
ax1=fig.add_subplot(1,1,1)
ax1.hist(x1,bins=100,color='darkgreen')
ax1.hist(x2,bins=100,color='orange',alpha=0.5)
ax1.xaxis.set_ticks_position('bottom')
ax1.yaxis.set_ticks_position('left')

plt.xlabel('Bins')
plt.ylabel('Data size of Values in Bin')
fig.suptitle('Histograms',fontsize=14,fontweight='bold')
ax1.set_title('Two Frequency data')

plt.savefig('histogram.png',dpi=400,bbox_inches='tight')
plt.show()
