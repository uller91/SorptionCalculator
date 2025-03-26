import math

from auxiliary_functions import find_value_from_function

#Ref: J. Huang, A Simple Accurate Formula for Calculating Saturation Vapor Pressure of Water and Ice, https://doi.org/10.1175/JAMC-D-17-0334.1
#Applicable in the range from -100 to +100C

def pressure_from_temperature(T_c):
    p_pa = math.exp(34.494-4924.99/(T_c+237.1))/math.pow((T_c+105), 1.57)
    p_mbar = p_pa/100
    return p_mbar

def temperature_from_pressure(p_mbar):
    increment = 1.0 #dT = 1C
    T_0 = 0 #C
    return find_value_from_function(p_mbar, pressure_from_temperature, increment, T_0)

