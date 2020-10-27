import Izracun
import numpy as np

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

podatki = {
    'L': 1,  # m
    'W': 0.70,  # m
    'q': 15,  # W/m2
    'n': 1,  # /
    'T1': 320,  # K
    'k': 0.35,  # W/mK
}
step = 0.1

x = np.arange(0, podatki["L"]+step, step)
y = np.arange(0, podatki["W"]+step, step)

X,Y = np.meshgrid(x,y)
nu = Izracun.izracun(X, Y, **podatki)

fig = plt.figure()
ax = Axes3D(fig)
ax.plot_surface(X,Y, nu)
plt.xlabel('b')
plt.ylabel('d')
plt.show()

