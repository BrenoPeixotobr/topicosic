##################################################
#  Reescrever a função objetivo Rosen de forma   #
#  a receber qualquer  quantidade/dimensão de x. #
##################################################

import matplotlib.pyplot as plt 
from mpltoolkits.mplot3d import Axes3D
import numpy as np
from scipy.optimize import minimize

def rosen2(x):
    return sum( 100 * x[1:] - x[:-1] ** 2 + (x[:-1] -1)**2 )

x0 = np.array([1000, 1000, 1000, 1000])
res = minimize(rosen2, x0)
print(res.x)
print(res.fun)