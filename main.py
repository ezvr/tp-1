import Izracun


def entry():
    # TREBA NARDIT DA SE LAHKO VNESE PODATKE
    podatki = {
        'L' : 0.70,  # m
        'W' : 0.70,  # m
        'q' : 15,  # W/m2
        'n': 1,  # /
        'T1' : 320,  # K
        'k' : 0.35,  # W/mK
    }
    step = 0.05
    ime = 'Erazem Zver'

    izrisi_graf(podatki, step, ime)


def izrisi_graf(podatki, step: float,ime):
    import numpy as np
    import matplotlib.pyplot as plt
    import os

    xarray = np.arange(0, podatki["L"]+step, step)
    yarray = np.arange(0, podatki["W"]+step, step)
    result = []

    # Pravilno oblikovanje podatkov
    for x in xarray:
        y_ar = []
        for y in yarray:
            y_ar.append(Izracun.izracun(x, y, **podatki))
        result.append(y_ar)
    nparray = np.array(result)
    X, Y = np.meshgrid(xarray, yarray)

    # Izrišemo graf
    plt.contourf(Y, X, nparray, 8, cmap='plasma')  # cmap -> barvna lestvica
    plt.grid(alpha=0.2)  # alpha ->prosojnost črt
    plt.xlabel('X-os')
    plt.ylabel('Y-os')
    plt.title(ime)
    plt.colorbar()
    dir_path = os.path.dirname(os.path.realpath(__file__))
    cntr = plt.contour(Y, X, nparray, 8, colors='white', linewidths=.5)

    plt.clabel(cntr, inline_spacing=1, fmt='%.2f', fontsize=10)

    plt.savefig(dir_path+'/fig1.png')


entry()
