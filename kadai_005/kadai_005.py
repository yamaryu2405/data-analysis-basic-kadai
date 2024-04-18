import numpy as np
import matplotlib.pyplot as plt

x1=[0,1,2,3]
y1=[1,2,-4,2]

x2=np.linspace(0,10,100)
y2= 2+2*np.sin(2*x2)

x3=np.random.normal(15,4,2000)

np.random.seed(0)
x4 = 5+np.random.normal(0,2,60)
y4 = 4+np.random.normal(0,2,len(x4))

fig, ax =plt.subplots(2,3,tight_layout=True)
ax[0,0].plot(x1,y1)
ax[0,1].plot(x2,y2)
ax[0,2].hist(x3)
ax[1,0].scatter(x4,y4)

ax[0,0].set(xlim=(0,3),ylim=(-5.5,3),xticks=np.arange(0,3,2) ,yticks=np.arange(-4,3,2))
ax[0,1].set(xlim=(0,10),ylim=(0.6),xticks=np.arange(0,10) ,yticks=np.arange(-1,6))
ax[0,2].set(xlim=(0,30),xticks=[0,20],yticks=[0,200,400])
ax[1,0].set(xlim=(0,10),ylim=(-1.8),xticks=np.arange(0,10,5) ,yticks=np.arange(0,8,2.5))

plt.show()