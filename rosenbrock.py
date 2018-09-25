import matplotlib.pyplot as plt 
from mpltoolkits.mplot3d import Axes3D
import numpy as np
from scipy.optimize import minimize

def rosen (x): ##########################
    x1 = x[1]
    x2 = x[2]
    return (x1 - x2 ** 2.0 ) ** 2.0    

x1 = np.arange(-2, 3)
x2 = np.arange(-2, 3)

y = rosen([x1, x2])
print(y)

fig = plt.figure()
ax=fig.gca(projection = '3d')
ax.plot(x1, x2, y)

### minimizar a funcao rosen ::

x0 = np.arrays([-100, -100]) #substituir por [-10000, -10000]
res = minimize(rosen, x0)
print(res.x) # =~ 1
print(res.fun) # =~ 0
