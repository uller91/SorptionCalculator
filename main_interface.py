from calculator_water_pressure import pressure_from_temperature, temperature_from_pressure
from calculator_adsorption_potential import calculate_adsorption_potential, uptake_from_adsorption_potential
from calculator_isobar import calculate_isobar
from calculator_cycle import calculate_cycle
from write_data import write_data_into_file
import os.path
import os

def initiate_the_interface(path_from, path_to, df_curve_file, df_curve_ext):
    #this fucntion exist to contorl file paths to make all the subroutine signatures clean

    #these file paths are:
    global file_path_df_curve
    global file_path_to
    global file_path_to_df #df curve subfolder inside file_path_to

    df_curve_ext = ".csv" #The code is working with .csv
    df_curve = df_curve_file + df_curve_ext
    file_path_df_curve = os.path.join(path_from, df_curve)
    file_path_to = path_to
    file_path_to_df = os.path.join(path_to, df_curve_file)

    run_the_interface()


def run_cycle_calculator():
    print("Cycle parameters calculator")
    mode = input("Choose three (3T) or four (4T) temperatures cycle: ")
    match mode.lower():
        case "3t":
            T_1 = float(input("Enter high temperature in Celcius: "))
            T_2 = float(input("Enter medium temperature in Celcius: "))
            T_3 = float(input("Enter low temperature in Celcius: "))
            calculate_cycle(T_1, T_2, T_2, T_3, file_path_df_curve, file_path_to_df)
        case "4t":
            T_1 = float(input("Enter high temperature in Celcius: "))
            T_2 = float(input("Enter condencer temperature in Celcius: "))
            T_2_S = float(input("Enter adsorption temperature in Celcius: "))
            T_3 = float(input("Enter evaporator temperature in Celcius: "))
            calculate_cycle(T_1, T_2, T_2_S, T_3, file_path_df_curve, file_path_to_df)
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
            pressure = pressure_from_temperature(temperature)
            calculate_isobar(pressure, file_path_df_curve, file_path_to_df)
            pressure_round = round(pressure, 2)
            print(f"\n{pressure_round} mbar isobar created!")
        case "p":
            pressure = float(input("Enter the pressure for the isobar in mbar: "))
            calculate_isobar(pressure, file_path_df_curve, file_path_to_df)
            print(f"\n{pressure} mbar isobar created!")
        case _:
            print("\nWrong mode!")
    repeat_or_abort(3)
    return

def run_adsorption_potential_calculator():
    print("Adsorption potential calculator")
    mode = input("Choose the calculation mode: T, P, PP0, cycle, uptake: ")
    match mode.lower():
        case "t":
            T_1 = float(input("Enter high temperature in Celcius: "))
            T_2 = float(input("Enter low temperature in Celcius: "))
            dF = calculate_adsorption_potential(T_2)(T_1)
            dF_round = round(dF, 2)
            print(f"\nCalculated adsorption potential for {T_1}C and {T_2}C is {dF_round} J/mol")
            
            p = pressure_from_temperature(T_2)
            p_round = round(p, 2)
            p0 = pressure_from_temperature(T_1)
            pp0_round = round(p/p0, 2)

            data = [dF_round, T_1, T_2, p_round, pp0_round]
            write_data_into_file(2, data, file_path_to=file_path_to)
        case "p":
            T_1 = float(input("Enter high temperature in Celcius: "))
            p = float(input("Enter pressure of the low temperature source in mbar: "))
            dF = calculate_adsorption_potential(pressure=p)(T_1)
            dF_round = round(dF, 2)
            print(f"\nCalculated adsorption potential for {T_1}C and {p} mbar is {dF_round} J/mol")
            
            T_2 = temperature_from_pressure(p)
            T_2_round = round(T_2, 2)
            p0 = pressure_from_temperature(T_1)
            pp0_round = round(p/p0, 2)

            data = [dF_round, T_1, T_2_round, p, pp0_round]
            write_data_into_file(2, data, file_path_to=file_path_to)
        case "pp0":
            T_1 = float(input("Enter high temperature in Celcius: "))
            pp0 = float(input("Enter P/P0: "))
            dF = calculate_adsorption_potential(PP0=pp0)(T_1)
            dF_round = round(dF, 2)
            print(f"\nCalculated adsorption potential for {T_1}C and {pp0} is {dF_round} J/mol")

            p0 = pressure_from_temperature(T_1)
            p = pp0 * p0
            p_round = round(p, 2)
            T_2 = temperature_from_pressure(p)
            T_2_round = round(T_2, 2)

            data = [dF_round, T_1, T_2_round, p_round, pp0]
            write_data_into_file(2, data, file_path_to=file_path_to)
        case "cycle":
            T_1 = float(input("Enter high temperature in Celcius: "))
            T_2 = float(input("Enter medium temperature in Celcius: "))
            T_3 = float(input("Enter low temperature in Celcius: "))
            dF_right = calculate_adsorption_potential(T_2)(T_1)
            dF_right_round = round(dF_right, 2)
            dF_left = calculate_adsorption_potential(T_3)(T_2)
            dF_left_round = round(dF_left, 2)
            print(f"\nCalculated adsorption potential for the right boundary of the cycle is {dF_right_round} J/mol")
            print(f"Calculated adsorption potential for the left boundary of the cycle is {dF_left_round} J/mol")
            
            data = [dF_right_round, dF_left_round, T_1, T_2, T_3]
            write_data_into_file(2, data, mode=mode, file_path_to=file_path_to)
        case "uptake": #add write data - write into the dF folder
            dF = float(input("Enter desired dF value: "))
            dF_round = round(dF, 2)
            uptake = uptake_from_adsorption_potential(dF, file_path_df_curve)
            uptake_round = round(uptake, 2)
            print(f"\nCalculated uptake from adsorption potential {dF_round} J/mol is {uptake_round} g/g")

            data = [dF_round, uptake_round]
            write_data_into_file(2, data, mode=mode, file_path_to_df=file_path_to_df)
        case _:
            print("\nWrong mode!")
    repeat_or_abort(2)
    return

def run_pressure_calculator():
    print("Pressure calculator")
    mode = input("Choose the value to calculate: P, T: ")
    match mode.lower():
        case "p":
            T_c = float(input("Enter temperature in Celcius: "))
            T_k = T_c + 273.15 #C to K
            p_mbar = pressure_from_temperature(T_c)
            p_mbar_round = round(p_mbar, 2)
            print(f"\nCalculated pressure for {T_c}C ({T_k}K) is {p_mbar_round} mbar")
            data = [T_c, p_mbar_round]
            write_data_into_file(1, data, file_path_to=file_path_to)
        case "t":
            p_mbar = float(input("Enter pressure in mbar: "))
            T_c = temperature_from_pressure(p_mbar)
            T_c_round = round(T_c, 2)
            print(f"\nCalculated temperature for {p_mbar} mbar is {T_c_round}C")
            data = [T_c_round, p_mbar]
            write_data_into_file(1, data, file_path_to=file_path_to)
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
            run_the_interface()

def run_the_interface():
    print("Welcome to the sorption calculator.")
    print(f"The cauclations are being performed usign {file_path_df_curve} file.")
    print("")
    print("Available subroutines:")
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
            run_the_interface()