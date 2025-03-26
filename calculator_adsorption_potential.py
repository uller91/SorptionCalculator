import math

from calculator_water_pressure import pressure_from_temperature
from auxiliary_functions import find_closest_to_value_v2, find_value_from_function

def uptake_from_adsorption_potential(dF, file_path):
    f = open(file_path, "r")
    content = f.readlines()
    w_vs_T = [] #uptake vs T curve
    for i in range(len(content)):
        if i != 0:
            line = content[i].split(", ")
            #print(line[0])
            #print(line[1])
            w_vs_T.append([float(line[0]), float(line[1])]) #w and dF

    w_found = find_closest_to_value_v2(float(dF), w_vs_T, 1, 0, True)

    f.close()
    return w_found

def calculate_adsorption_potential(T_2 = None, pressure = None, PP0 = None): #T_1 > T_2
    # currying to satisfy the find_closest_to_value_v2() signature for funstion
    def inner_function(T_1):
        dF = 0 #J/mol
        R_gas = 8.3144598 #universal gas constant
    
        if T_2 != None:
            p_1 = pressure_from_temperature(T_1)
            p_2 = pressure_from_temperature(T_2)
            dF = -R_gas * (T_1 + 273.15) * math.log(p_2/p_1)

        if pressure != None:
            p_1 = pressure_from_temperature(T_1)
            dF = -R_gas * (T_1 + 273.15) * math.log(pressure/p_1)

        if PP0 != None:
            dF = -R_gas * (T_1 + 273.15) * math.log(PP0)

        return dF
    return inner_function

def temperature_from_adsorption_potential_and_pressure(dF, p): #calculates T_1 from dF and pressure
    increment = 1.0 #dT = 1C
    T_0 = 0 #C
    function = calculate_adsorption_potential(pressure=p)
    return find_value_from_function(dF, function, increment, T_0)