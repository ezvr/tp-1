import Izracun
import numpy as np

L = 0.8
W = 0.8

xarray = np.arange(0,L,0.1)
yarray = np.arange(0,W,0.1)



result = []

for x in xarray:
    y_ar = []
    for y in yarray:
        print(x,y)
        print(Izracun.izracun(x,y))
        y_ar.append(Izracun.izracun(x,y))
    result.append(y_ar)



for x in result:
    print(max(x))
