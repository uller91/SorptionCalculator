import math


#Ref: J. Huang, A Simple Accurate Formula for Calculating Saturation Vapor Pressure of Water and Ice, https://doi.org/10.1175/JAMC-D-17-0334.1
#Applicable in the range from -100 to +100C

def calculate_pressure(T_c):
    p_pa = math.exp(34.494-4924.99/(T_c+237.1))/math.pow((T_c+105), 1.57)
    p_mbar = p_pa/100
    return p_mbar

def calculate_temperature(p_mbar):
    increment = 1.0 #dT = 1C
    T_0 = 0 #C
    return calculate_temperature_r(p_mbar, T_0, increment)

def calculate_temperature_r(p, T_current, increment): #approaching the goal from one side
    p_current = calculate_pressure(T_current)
    
    if p_current > p:
        T_current -= increment
        increment /= 10

    if increment <= 0.0001: #breaking the loop
        return T_current
    
    T_current += increment
    return calculate_temperature_r(p, T_current, increment)

"""
def main():
    print("Pressure calculator")
    T_c = float(input("Enter temperature in Celcius: "))
    T_k = T_c + 273.15 #C to K
    p_mbar = format(calculate_pressure(T_c), ".2f")
    print(f"Calculated pressure for {T_c}C ({T_k}K) is {p_mbar} mbar")
"""

#main()
