import numpy as np


def izracun(x, y, q, L, T1, k, W, n):
    """Izračunaj vrednost temperature pri podanih podatkih.

    Keyword arguments:
    x -- premik v x smeri [m] (default 0.0)
    y -- premik v y smeri [m] (default 0.0)
    """

    A = 2 * q * L * (1 - (-1)**n)
    B = k * n**2 * np.pi**2 * np.cosh((n * np.pi * W) / L)
    C = np.sin((n * np.pi * x) / L)
    D = np.sinh((n * np.pi * y) / L)

    T_x_y = T1 + (A / B) * C * D

    # n=1

    rezultat = T_x_y

    return rezultat
