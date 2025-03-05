import math

from pressure import calculate_pressure
from auxiliary_functions import find_closest_to_value as find_closest


def uptake_from_adsorption_potential(dF, file_path):
    f = open(file_path, "r")
    content = f.readlines()
    w_vs_T = [] #uptake vs T curve
    for i in range(len(content)):
        if i != 0:
            line = content[i].split()
            #print(line[0])
            #print(line[1])
            w_vs_T.append([float(line[0]), float(line[1])]) #w and dF

    w_found = find_closest(float(dF), w_vs_T)

    f.close()
    return w_found

def calculate_adsorption_potential(T_1, T_2 = None, pressure = None, PP0 = None): #T_1 > T_2
    dF = 0 #J/mol
    R_gas = 8.3144598 #universal gas constant
    
    if T_2 != None:
        p_1 = calculate_pressure(T_1)
        p_2 = calculate_pressure(T_2)
        dF = -R_gas * (T_1 + 273.15) * math.log(p_2/p_1)

    if pressure != None:
        p_1 = calculate_pressure(T_1)
        dF = -R_gas * (T_1 + 273.15) * math.log(pressure/p_1)

    if PP0 != None:
        dF = -R_gas * (T_1 + 273.15) * math.log(PP0)

    return dF
    
def temperature_from_adsorption_potential_and_pressure(dF, p): #calculates T_1 from dF and pressure
    increment = 1.0 #dT = 1C
    T_0 = 0 #C
    return temperature_from_adsorption_potential_and_pressure_r(dF, p, T_0, increment)

def temperature_from_adsorption_potential_and_pressure_r(dF, p, T_current, increment): #approaching the goal from one side
    dF_current = calculate_adsorption_potential(T_current, pressure = p)
    
    if dF_current > dF:
        T_current -= increment
        increment /= 10

    if increment <= 0.0001: #breaking the loop
        return T_current
    
    T_current += increment
    return temperature_from_adsorption_potential_and_pressure_r(dF, p, T_current, increment)

"""
def main():
    print("Adsorption potential calculator")
    mode = input("Choose the calculation mode: T, P or PP0: ")
    match mode:
        case "T":
            T_1 = float(input("Enter high temperature in Celcius: "))
            T_2 = float(input("Enter low temperature in Celcius: "))
            dF = format(calculate_adsorption_potential(T_1, T_2), ".2f")
            print(f"Calculated adsorption potential for {T_1}C and {T_2}C is {dF} J/mol")
        case "P":
            T_1 = float(input("Enter high temperature in Celcius: "))
            p = float(input("Enter pressure of the low temperature source in mbar: "))
            dF = format(calculate_adsorption_potential(T_1, pressure=p), ".2f")
            print(f"Calculated adsorption potential for {T_1}C and {p} mbar is {dF} J/mol")
        case "PP0":
            T_1 = float(input("Enter high temperature in Celcius: "))
            pp0 = float(input("Enter P/P0: "))
            dF = format(calculate_adsorption_potential(T_1, PP0=pp0), ".2f")
            #dF = format(calculate_adsorption_potential(T_1, pressure==relative_pressure), ".2f")
            print(f"Calculated adsorption potential for {T_1}C and {pp0} is {dF} J/mol")
"""

#def main():
#    print(uptake_from_adsorption_potential(250, "w_vs_dF.txt"))

#main()