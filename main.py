import Izracun


def entry():
    # TREBA NARDIT DA SE LAHKO VNESE PODATKE
    L = 0.70  # m
    W = 0.70  # m
    step = 0.05

    izrisi_graf(L, W, step)


def izrisi_graf(L: float, W: float, step: float):
    import numpy as np
    import matplotlib.pyplot as plt
    import os

    xarray = np.arange(0, L+step, step)
    yarray = np.arange(0, W+step, step)
    result = []

    # Pravilno oblikovanje podatkov
    for x in xarray:
        y_ar = []
        for y in yarray:
            y_ar.append(Izracun.izracun(x, y))
        result.append(y_ar)
    nparray = np.array(result)
    X, Y = np.meshgrid(xarray, yarray)

    # Izrišemo graf
    plt.contourf(Y, X, nparray, 8, cmap='plasma')  # cmap -> barvna lestvica
    plt.grid(alpha=0.2)  # alpha ->prosojnost črt
    plt.xlabel('X-os')
    plt.ylabel('Y-os')
    plt.title('Jaka Purič, 23202024')
    plt.colorbar()
    dir_path = os.path.dirname(os.path.realpath(__file__))
    cntr = plt.contour(Y, X, nparray, 8, colors='white', linewidths=.5)

    plt.clabel(cntr, inline_spacing=1, fmt='%.2f', fontsize=10)

    plt.savefig(dir_path+'/fig1.png')


entry()
