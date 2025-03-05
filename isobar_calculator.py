from adsorption_potential import temperature_from_adsorption_potential_and_pressure as df_to_t


def isobar_calculator(p, file_path):
    f = open(file_path, "r")
    content = f.readlines()
    file_name = format(p, ".2f")
    n_f = open(f"calculated\Isobar_{file_name}_mbar.csv", "w+")
    n_f.write(f"Isobar, {file_name}, mbar\n")

    for i in range(len(content)):
        line = content[i].split()
        if i == 0:
           line.append("T\n")
        else:
           line.append(str(df_to_t(float(line[1]), p)) + "\n")
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