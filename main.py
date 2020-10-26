import Izracun
import numpy as np
import matplotlib.pyplot as plt
import os


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




nparray = np.array(result)


X, Y = np.meshgrid(xarray, yarray)
ax = plt.contourf(Y,X, nparray,50)

dir_path = os.path.dirname(os.path.realpath(__file__))

plt.savefig(dir_path+'/fig1.png')

