# Wavicle - determine the De Broglie wavelength of any massive particle
# Tristan Manchester and William Pearson
# github.com/tristanmanchester
# github.com/WilliamMAPearson

import math


def main():
    mass = particle_select()
    energy = energy_select(mass)
    print(calculator(energy, mass))


def particle_select():
    print('You may choose from a proton, neutron, electron, or muon. You may also enter the mass of a custom particle '
          'in the format xEy. Units are eV or kg.')
    mass = None
    while True:
        particle = input('Choose your particle or enter a mass: ').lower()
        if (particle == 'proton' or particle == 'neutron' or particle == 'electron' or particle == 'muon' or
                (particle.split('e')[0].replace('.', '', 1).isdigit() and particle.split('e')[1].replace('.', '',
                                                                                                         1).isdigit())):
            break
    if particle.isalpha():
        if particle == 'electron':
            mass = 510.99895000 * 10 ** 3
        elif particle == 'proton':
            mass = 938.27208816 * 10 * 6
        elif particle == 'neutron':
            mass = 939.56542052 * 10 ** 6
        elif particle == 'muon':
            mass = 105.6583755 * 10 ** 6
    else:
        while True:
            units = input('Enter your units, eV or kg: ').lower()
            if units == 'ev' or units == 'kg':
                break
        custom_mass = particle.split('e')
        mass = float(custom_mass[0]) * 10 ** float(custom_mass[1])
        if units == 'kg':
            mass = unit_converter(mass, units)
    return mass


def unit_converter(v, u, m=1):
    if u == 'kg':
        m = v * 5.60958860380445e35
        return m
    if u == 'j':
        e = v * 6.2415093433e18
        return e
    if u == 'm/s':
        e_j = 0.5 * m * v ** 2
        e = e_j * 6.242e18
        return e


def energy_select(m):
    choice = None
    unit = None
    while True:
        e_or_v = input('Do you want to use energy or velocity? ').lower()
        if e_or_v == 'energy' or e_or_v == 'velocity':
            break
    if e_or_v == 'energy':
        choice = 'energy'
        while True:
            unit = input('eV or J? ').lower()
            if unit == 'ev' or unit == 'j':
                break
    elif e_or_v == 'velocity':
        choice = 'velocity'
        unit = 'm/s'
    while True:
        value = input(f'Enter the {choice} ({unit}) in the format xEy: ').lower().split('e')
        if value[0].replace('.', '', 1).isdigit() and value[1].replace('.', '', 1).isdigit():
            break
    value = float(value[0]) * 10 ** float(value[1])
    if unit == 'm/s' or unit == 'j':
        energy = unit_converter(value, unit, m)
    else:
        energy = value
    return energy


def calculator(e, m):
    h = 4.1356677e-15
    c = 3e8
    wavelength = h / math.sqrt(2 * (m / (c ** 2)) * e)
    return f'The De Broglie wavelenth of your particle is {wavelength * (10 ** 9)} nm'


if __name__ == '__main__':
    main()
