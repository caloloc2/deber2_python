import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

datos = np.zeros((10, 2))
x=0

for x in range(0, 10):
    muestra = norm.rvs(size=10000)
    v_l = np.sum((muestra - np.mean(muestra))**2)/10000
    v_c = np.sum((muestra - np.mean(muestra))**2)/(10000-1)
    datos[x,0] = v_l
    datos[x,1] = v_c
    x+= 1

print (datos)

plt.plot(datos, '-r', linewidth=1)
plt.show()