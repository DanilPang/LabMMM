import numpy as np
import matplotlib.pyplot as plt

a=np.loadtxt('Newton2.txt')
a0=np.loadtxt("Newton20.txt")
plt.plot(a[:,0],a[:,1],a0[:,0],a0[:,1], 'ro')
plt.grid()
plt.show()
