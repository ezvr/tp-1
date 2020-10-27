def __main__():
    # TREBA NARDIT DA SE LAHKO VNESE PODATKE ?
    podatki = {
        'L': 1,  # m
        'W': 1,  # m
        'q': 15,  # W/m2
        'n': 1,  # /
        'T1': 320,  # K
        'k': 0.35,  # W/mK
    }
    step = 0.1
    ime = 'Erazem Zver'

    izrisi_graf(podatki, step, ime)


def izrisi_graf(podatki, step: float, ime):
    import Izracun  # Uvozimo datoteko Izračun.py
    import numpy as np
    import matplotlib.pyplot as plt
    import os

    # Izračun
    x = np.arange(0, podatki["L"]+step, step)
    y = np.arange(0, podatki["W"]+step, step)
    X, Y = np.meshgrid(x, y)
    result = Izracun.izracun(X, Y, **podatki)

    # Izrišemo graf
    plt.contourf(X, Y, result, 8, cmap='plasma')  # cmap -> barvna lestvica
    plt.grid(alpha=0.2)  # alpha ->prosojnost črt
    plt.xlabel('X-os')
    plt.ylabel('Y-os')
    plt.title(ime)
    plt.colorbar()
    cntr = plt.contour(X, Y, result, 8, colors='white', linewidths=.5)
    plt.clabel(cntr, inline_spacing=1, fmt='%.2f', fontsize=10)

    # Shranimo graf v sliko
    # Določimo mapo v kateri je main.py
    dir_path = os.path.dirname(os.path.realpath(__file__))
    plt.savefig(dir_path+'/fig1.png')  # Shranimo v to mapo


# Pokličemo funkcijo __main__, ki sproži program
__main__()
