import numpy as np


def izracun(x: float = 0, y: float = 0):
    """Izračunaj vrednost temperature pri podanih podatkih.

    Keyword arguments:
    x -- premik v x smeri [m] (default 0.0)
    y -- premik v y smeri [m] (default 0.0)
    """

    print('jjaka')

    q = 15  # W/m2
    L = 0.7  # m
    n = 1  # /
    T1 = 320  # K
    k = 0.35  # W/mK
    W = 0.7  # m

    A = 2 * q * L * (1 - (-1)**n)
    B = k * n**2 * np.pi**2 * np.cosh((n * np.pi * W) / L)
    C = np.sin((n * np.pi * x) / L)
    D = np.sinh((n * np.pi * y) / L)

    T_x_y = (A / B) * C * D

    # n=1

    rezultat = T_x_y

    return rezultat
