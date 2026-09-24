import CoolProp
from CoolProp.CoolProp import PropsSI

def printH(val : float, str : str = ''):
    print(str, val/1000, 'kJ/kg')

def printS(val : float, str : str = ''):
    print(str, val/1000, 'kJ/kgK')

Cp_water = 4.186 # kJ/kgK

P_atm = 785.1e2 # Presion atmosferica
'''
    Propiedades a la salida de la caldera
'''
P1_man = 637_432.25 # Pa
X = 0.97 # Calidad de salida de la caldera
P1_abs = P1_man + P_atm
'''
    Propiedades pasando la valvula
'''
P2_man = 588_399 # Pa
P2_abs = P2_man + P_atm
'''
    Propiedades a la salida de la turbina o bien
    a la entrada del condensador
'''
P3_vac = 26_664.391305276 # Pa vacuometrica
T3_K = 73 + 273.15 # Kelvin
P3_abs = P_atm - P3_vac
'''
    Propiedades del pozo o bien a la salida de
    la turbina
'''
T4_C = 31
'''
    Propiedades a la salida de la entrada del 
    tanque de condensado
'''
T5_C = 36

# Entalpia del estado 1
h1 = PropsSI('H','P',P1_abs, 'Q', X, 'water')
    
# Proceso isentalpico de la valvula
h2 = h1

# Caida ideal isentropica hacia el estado 3
# por medio de P y H
s2 = PropsSI('S','P',P2_abs, 'H', h2, 'water')

s3 = s2
# Con esta entropia buscamos al estado 3 ideal
# por medio de la entropia
h3_isen = PropsSI('H','S',s3,'P',P3_abs, 'water')

# Para encontrar la h3 real utilizamos la p3 y t3
h3_real = PropsSI('H','T',T3_K, 'P', P3_abs, 'water')

# Para encontrar a h4 y h5 utilizamos la ecuacion de calor especifico
h4 = Cp_water*T4_C
h5 = Cp_water*T5_C

printH(h1, 'Entalpia del estado 1 : ')
printH(h2, 'Entalpia del estado 2 : ')
printS(s2, 'Entropia del estado 2 : ')
printH(h3_isen, 'Entalpia del estado 3 bajo un proceso ideal : ')
printH(h3_real, 'Entalpia del estado 3 bajo un proceso real : ')
printH(h4, 'Entalpia del estado 4 : ')
printH(h5, 'Entalpia del estado 5 : ')