from calculator_adsorption_potential import calculate_adsorption_potential, uptake_from_adsorption_potential, temperature_from_adsorption_potential_and_pressure
from calculator_isobar import calculate_isobar
from calculator_water_pressure import pressure_from_temperature
from write_data import write_data_into_file


def calculate_cycle(T_1, T_2, T_2_S, T_3, file_path_df_curve, file_path_to_df):
    if T_2 == T_2_S:
        print(f"Calculating parameters for the {T_3}/{T_2}/{T_1} cycle.")
    else:
        print(f"Calculating parameters for the {T_3}/{T_2_S} {T_2}/{T_1} cycle.")
    dF_right = calculate_adsorption_potential(T_2)(T_1)
    dF_right_round = round(dF_right, 2)
    dF_left = calculate_adsorption_potential(T_3)(T_2_S)
    dF_left_round = round(dF_left, 2)
    print(f"\nCalculated adsorption potential for the right boundary of the cycle is {dF_right_round} J/mol")
    print(f"Calculated adsorption potential for the left boundary of the cycle is {dF_left_round} J/mol")

    print("\nCalculating isobars...")
    right_isobar_pressure = pressure_from_temperature(T_2)
    calculate_isobar(right_isobar_pressure, file_path_df_curve, file_path_to_df)
    left_isobar_pressure = pressure_from_temperature(T_3)
    calculate_isobar(left_isobar_pressure, file_path_df_curve, file_path_to_df)

    w_1 = uptake_from_adsorption_potential(dF_right, file_path_df_curve)
    w_1_round = round(w_1, 3)
    w_2 = uptake_from_adsorption_potential(dF_left, file_path_df_curve)
    w_2_round = round(w_2, 3)
    print(f"Calculated desorption uptake w_1={w_1_round} g/g")
    print(f"Calculated adsorption uptake w_2={w_2_round} g/g")
    dw = w_2 - w_1
    dw_round = round(dw, 3)
    print(f"Cumulative cycle uptake dw={dw_round} g/g")

    T_s_i = temperature_from_adsorption_potential_and_pressure(dF_right, left_isobar_pressure)
    T_s_i_round = round(T_s_i, 1)
    T_d_i = temperature_from_adsorption_potential_and_pressure(dF_left, right_isobar_pressure)
    T_d_i_round = round(T_d_i, 1)
    print(f"\nCalculated initial adsorption temperature is {T_s_i_round}C")
    print(f"Calculated initial desorption temperature is {T_d_i_round}C")

    data = [T_1, T_2, T_2_S, T_3, dF_right_round, dF_left_round, w_1_round, w_2_round, dw_round, T_s_i_round, T_d_i_round]
    write_data_into_file(4, data, file_path_to_df=file_path_to_df)


