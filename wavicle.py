# Wavicle - determine the De Broglie wavelength of any massive particle
# Tristan Manchester and William Pearson
# github.com/tristanmanchester
# github.com/WilliamMAPearson

import math


def wavelength_finder():
    m = input('Mass of the particle in keV/c^2: ')
    e = input('Energy of the particle in keV : ')
    h = 4.126 * 10 ** (-18)  # keV.s
    c = 3 * 10 ** 8
    wavelength = h / math.sqrt(2 * (int(m)/(c**2)) * int(e))
    print(f'{wavelength*(10**9)} nm')


wavelength_finder()