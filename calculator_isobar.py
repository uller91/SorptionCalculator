import os.path

from calculator_adsorption_potential import temperature_from_adsorption_potential_and_pressure


def calculate_isobar(p, file_path_df_curve, file_path_to):
    f = open(file_path_df_curve, "r")
    content = f.readlines()
    file_name = format(p, ".2f")
    full_file_path_to = os.path.join(file_path_to, f"Isobar_{file_name}_mbar.csv")
    n_f = open(full_file_path_to, "w+")
    n_f.write(f"Isobar, {file_name}, mbar\n")

    for i in range(len(content)):
        line = (content[i].strip("\n")).split(", ")
        if i == 0:
           line.append("T\n")
        else:
           line.append(str(temperature_from_adsorption_potential_and_pressure(float(line[1]), p)) + "\n")
        n_f.write(", ".join(line))

    f.close()
    n_f.close()
    return

"""
def main():
    p = 12 #isobar pressure
    file_path = "w_vs_dF.txt"
    isobar_calculator(p, file_path)
"""

#main()