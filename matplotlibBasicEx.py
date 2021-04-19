import numpy as np
import matplotlib.pyplot as plt

plt.title("'rs--' style plot")
plt.plot([10,20,30,40],[1,4,9,16],'rs--')
plt.show()

plt.title("x axis and y axis range set")
plt.plot([10,20,30,40],[1,4,9,16],c='b',lw=5,ls="--",
         marker="o",ms=10,mec='g',mew=5,mfc='r')
plt.xlim(0,50)
plt.ylim(-10,30)
plt.show()

X=np.linspace(-np.pi,np.pi,256)
C=np.cos(X)
plt.title("x and y axis tick label set")
plt.plot(X,C)
plt.xticks([-np.pi,-np.pi/2.0,0,np.pi/2.0,np.pi])
plt.yticks([-1,0,1])
plt.show()

t=np.arange(0.,5.,0.2)
plt.plot(t,t,'r--',t,0.5*t**2,'bs:',t,0.2*t**3,'g^-')
plt.show()

S=np.sin(X)
plt.plot(X,C,ls='--',label='cosine')
plt.plot(X,S,ls=':',label='sine')
plt.legend(loc=2)
plt.show()
