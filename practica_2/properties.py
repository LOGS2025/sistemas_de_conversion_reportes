import CoolProp
from CoolProp.CoolProp import PropsSI

P3 = 785.1e2
Patm = P3
T3 = 120 + 273.15

P2 = 627.6256e3 + Patm

P4 = 245166.25 + Patm
T4 = 159 + 273.15

def printH(val : float, str : str = ''):
    print(str, val/1000, 'kJ/kg')

def printS(val : float, str : str = ''):
    print(str, val/1000, 'kJ/kgK')

h3 = PropsSI('H', 'T', T3, 'P', P3, 'water')
printH(h3, 'Entalpia del estado 3')
s3 = PropsSI('S', 'T', T3, 'P', P3, 'water')
printS(s3, 'Entropia del estado 3')


h2g = PropsSI('H', 'P', P2, 'Q', 1.0, 'water')
printH(h2g, 'Entalpia del estado de vapor saturado a presion 2')
h2f = PropsSI('H', 'P', P2, 'Q', 0.0, 'water')
printH(h2f, 'Entalpia del estado de liquido saturado a presion 2')

h4 = PropsSI('H', 'T', T4, 'P', P4, 'water')
printH(h4, 'Entalpia del estado 4')