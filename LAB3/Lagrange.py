import numpy as np
import matplotlib.pyplot as plt

a=np.loadtxt("Lagrange.txt")
a0=np.loadtxt("Lagrange0.txt")
plt.plot(a[:,0],a[:,1],a0[:,0],a0[:,1], 'ro')
plt.grid()
plt.show()
