import Izracun


def entry():
    # TREBA NARDIT DA SE LAHKO VNESE PODATKE
    L = 0.70  # m
    W = 0.70  # m
    step = 0.01

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
    plt.subplots()
    plt.contourf(Y, X, nparray, 15, cmap='jet')
    plt.grid(alpha=0.2)
    dir_path = os.path.dirname(os.path.realpath(__file__))
    cntr = plt.contour(Y, X, nparray, 15, colors='black', linewidths=.5)

    plt.clabel(cntr, inline_spacing=1, fmt='%.2f', fontsize=10)

    plt.savefig(dir_path+'/fig1.png')


entry()
