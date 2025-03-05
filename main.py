from pressure import calculate_pressure, calculate_temperature
from adsorption_potential import calculate_adsorption_potential
from adsorption_potential import temperature_from_adsorption_potential_and_pressure as df_to_t
from isobar_calculator import isobar_calculator
from calculate_cycle import calculate_cycle


def run_cycle_calculator():
    print("Cycle parameters calculator")
    mode = input("Choose three (3T) or four (4T) temperatures cycle: ")
    match mode.lower():
        case "3t":
            T_1 = float(input("Enter high temperature in Celcius: "))
            T_2 = float(input("Enter medium temperature in Celcius: "))
            T_3 = float(input("Enter low temperature in Celcius: "))
            calculate_cycle(T_1, T_2, T_2, T_3, df_curve_file_path)
        case "4t":
            T_1 = float(input("Enter high temperature in Celcius: "))
            T_2 = float(input("Enter condencer temperature in Celcius: "))
            T_2_S = float(input("Enter adsorption temperature in Celcius: "))
            T_3 = float(input("Enter evaporator temperature in Celcius: "))
            calculate_cycle(T_1, T_2, T_2_S, T_3, df_curve_file_path)
        case _:
            print("\nWrong mode!")
    repeat_or_abort(4)
    return

def run_isobar_calculator():
    print("Isobar from adsorption potential calculator")
    mode = input("Choose the isobar calculation mode: temperature of the water source (T) or pressure (P): ")
    match mode.lower():
        case "t":
            temperature = float(input("Enter the temperature for the isobar in C: "))
            pressure = calculate_pressure(temperature)
            isobar_calculator(pressure, df_curve_file_path)
            pressure_formatted = format(pressure, ".2f")
            print(f"\n{pressure_formatted} mbar isobar created!")
        case "p":
            pressure = float(input("Enter the pressure for the isobar in mbar: "))
            isobar_calculator(pressure, df_curve_file_path)
            print(f"\n{pressure} mbar isobar created!")
        case _:
            print("\nWrong mode!")
    repeat_or_abort(3)
    return

def run_adsorption_potential_calculator():
    print("Adsorption potential calculator")
    mode = input("Choose the calculation mode: T, P, PP0, cycle: ")
    match mode.lower():
        case "t":
            T_1 = float(input("Enter high temperature in Celcius: "))
            T_2 = float(input("Enter low temperature in Celcius: "))
            dF = calculate_adsorption_potential(T_1, T_2)
            dF_formatted = format(dF, ".2f")
            print(f"\nCalculated adsorption potential for {T_1}C and {T_2}C is {dF_formatted} J/mol")
        case "p":
            T_1 = float(input("Enter high temperature in Celcius: "))
            p = float(input("Enter pressure of the low temperature source in mbar: "))
            dF = calculate_adsorption_potential(T_1, pressure=p)
            dF_formatted = format(dF, ".2f")
            print(f"\nCalculated adsorption potential for {T_1}C and {p} mbar is {dF_formatted} J/mol")
        case "pp0":
            T_1 = float(input("Enter high temperature in Celcius: "))
            pp0 = float(input("Enter P/P0: "))
            dF = calculate_adsorption_potential(T_1, PP0=pp0)
            dF_formatted = format(dF, ".2f")
            #dF = format(calculate_adsorption_potential(T_1, pressure==relative_pressure), ".2f")
            print(f"\nCalculated adsorption potential for {T_1}C and {pp0} is {dF_formatted} J/mol")
        case "cycle":
            T_1 = float(input("Enter high temperature in Celcius: "))
            T_2 = float(input("Enter medium temperature in Celcius: "))
            T_3 = float(input("Enter low temperature in Celcius: "))
            dF_right = calculate_adsorption_potential(T_1, T_2)
            dF_right_formatted = format(dF_right, ".2f")
            dF_left = calculate_adsorption_potential(T_2, T_3)
            dF_left_formatted = format(dF_left, ".2f")
            print(f"\nCalculated adsorption potential for the right boundary of the cycle is {dF_right_formatted} J/mol")
            print(f"Calculated adsorption potential for the left boundary of the cycle is {dF_left_formatted} J/mol")
        case _:
            print("\nWrong mode!")
            #raise Exception("wrong mode")
    repeat_or_abort(2)
    return

def run_pressure_calculator():
    print("Pressure calculator")
    mode = input("Choose the value to calculate: P, T: ")
    match mode.lower():
        case "p":
            T_c = float(input("Enter temperature in Celcius: "))
            T_k = T_c + 273.15 #C to K
            p_mbar = calculate_pressure(T_c)
            p_mbar_formatted = format(p_mbar, ".2f")
            print(f"\nCalculated pressure for {T_c}C ({T_k}K) is {p_mbar_formatted} mbar")
        case "t":
            p_mbar = float(input("Enter pressure in mbar: "))
            T_c = calculate_temperature(p_mbar)
            T_c_formatted = format(T_c, ".2f")
            print(f"\nCalculated temperature for {p_mbar} mbar is {T_c_formatted}C")
    repeat_or_abort(1)
    return

def repeat_or_abort(n):
    print("")
    subroutine = input("Repeat (r), Quit (q) or Restart (anything else)? ")
    match subroutine.lower():
        case "r":
            if n == 1:
                run_pressure_calculator()
            if n == 2:
                run_adsorption_potential_calculator()
            if n == 3:
                run_isobar_calculator()
            if n == 4:
                run_cycle_calculator()
        case "q":
            print("Thank you for using the sorption calculatior today!\n")
            exit(0)
        case _:
            running_the_subroutine()

def running_the_subroutine():
    print("")
    print("1 - Pressure calculator")
    print("2 - Adsorption potential calculator")
    print("3 - Isobar calculator")
    print("4 - Cycle parameters calculator")
    print("")
    subroutine = input("Enter the desired subroutine (1-4; q - to exit): ")
    print("")

    match subroutine.lower():
        case "1":
            run_pressure_calculator()
        case "2":
            run_adsorption_potential_calculator()
        case "3":
            run_isobar_calculator()
        case "4":
            run_cycle_calculator()
        case "q":
            print("Thank you for using the sorption calculatior today!\n")
            exit(0)
        case _:
            print("Such subroutine doesn't exist!")


def main():
    global df_curve_file_path 
    df_curve_file_path = "data\w_vs_dF_B300_35CaCl2.txt" #dF curve file path
    
    print("Welcome to the sorption calculator. Available subroutines:")
    
    running_the_subroutine()
    

main()
