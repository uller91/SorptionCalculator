from adsorption_potential import calculate_adsorption_potential, uptake_from_adsorption_potential, temperature_from_adsorption_potential_and_pressure
from isobar_calculator import isobar_calculator
from pressure import calculate_pressure


def calculate_cycle(T_1, T_2, T_2_S, T_3, df_curve_file_path):
    if T_2 == T_2_S:
        print(f"Calculating parameters for the {T_3}/{T_2}/{T_1} cycle.")
    else:
        print(f"Calculating parameters for the {T_3}/{T_2_S} {T_2}/{T_1} cycle.")
    dF_right = calculate_adsorption_potential(T_1, T_2)
    dF_right_formatted = format(dF_right, ".2f")
    dF_left = calculate_adsorption_potential(T_2_S, T_3)
    dF_left_formatted = format(dF_left, ".2f")
    print(f"\nCalculated adsorption potential for the right boundary of the cycle is {dF_right_formatted} J/mol")
    print(f"Calculated adsorption potential for the left boundary of the cycle is {dF_left_formatted} J/mol")

    print("\nCalculating isobars...")
    right_isobar_pressure = calculate_pressure(T_2)
    isobar_calculator(right_isobar_pressure, df_curve_file_path)
    left_isobar_pressure = calculate_pressure(T_3)
    isobar_calculator(left_isobar_pressure, df_curve_file_path)

    w_1 = uptake_from_adsorption_potential(dF_right, df_curve_file_path)
    w_1_formatted = format(w_1, ".3f")
    w_2 = uptake_from_adsorption_potential(dF_left, df_curve_file_path)
    w_2_formatted = format(w_2, ".3f")
    print(f"Calculated desorption uptake w_1={w_1_formatted} g/g")
    print(f"Calculated adsorption uptake w_2={w_2_formatted} g/g")
    dw = w_2 - w_1
    dw_formatted = format(dw, ".3f")
    print(f"Cumulative cycle uptake dw={dw_formatted} g/g")

    T_s_i = temperature_from_adsorption_potential_and_pressure(dF_right, left_isobar_pressure)
    T_s_i_formatted = format(T_s_i, ".1f")
    T_d_i = temperature_from_adsorption_potential_and_pressure(dF_left, right_isobar_pressure)
    T_d_i_formatted = format(T_d_i, ".1f")
    print(f"\nCalculated initial adsorption temperature is {T_s_i_formatted}C")
    print(f"Calculated initial desorption temperature is {T_d_i_formatted}C")


