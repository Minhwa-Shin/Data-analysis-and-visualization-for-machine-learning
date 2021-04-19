import matplotlib.pyplot as plt
import numpy as np

x1=np.linspace(0.0,5.0)
y1=np.cos(2*np.pi*x1)*np.exp(-x1)

x2=np.linspace(0.0,2.0)
y2=np.cos(2*np.pi*x2)

ax1=plt.subplot(2,1,1) #2X1
plt.plot(x1,y1,'yo-')
plt.title("plots of 2 subplots")
plt.ylabel('flow data')

ax2=plt.subplot(2,1,2)
plt.plot(x2,y2,'r.-')
plt.xlabel('time (s)')
plt.ylabel('result')
plt.tight_layout()
plt.show()
