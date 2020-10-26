import Izracun
import numpy as np
import matplotlib.pyplot as plt


L = 0.71
W = 0.71

xarray = np.arange(0,L,0.01)
yarray = np.arange(0,W,0.01)



result = []

for x in xarray:
    y_ar = []
    for y in yarray:
        y_ar.append(Izracun.izracun(x,y))
    result.append(y_ar)


for x in result:
    print(max(x))

nparray = np.array(result)


X, Y = np.meshgrid(xarray, yarray)
ax = plt.contourf(Y,X, nparray,50)
plt.savefig('C:/Users/Zver/Code/TP-1/fig.png')

