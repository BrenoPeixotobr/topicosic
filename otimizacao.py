
import numpy as np 
import matplotlib.pyplot as plt
from scipy.optimize import  minimize

def quad(x):
    return (x*x) # x*x + x

x = np.arange(-10, 11)
y = quad(x)

print(x)
print(y)

plt.plot(x, y)

x0 = -10

resultado = minimize(quad, x0)
print(resultado.x)