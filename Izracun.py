import numpy as np


def izracun():
    print('jjaka')

    q = 15  # W/m2
    L = 0.7  # m
    n = 1  # /
    x = 0  # m
    y = 0  # m
    T1 = 320  # K
    k = 0.35  # W/mK

    # n=1
    T_x_y = ((2*q*L*(1-(-1) ^ n)) / (k*(n) ^ 2 *
                                     (np.pi) ^ 2 * np.cosh*((n*np.pi * y)/L)))

    rezultat = T_x_y

    return rezultat
