import os.path
import os

def write_data_into_file(subroutine, data, mode = None, file_path_to = None):
    #receives .2f formatted data at the moment
    data_folder = "calculated"

    match subroutine:
        case 1:
            file_path = os.path.join(data_folder, "calculator_pressure_results.csv")
            if not os.path.isfile(file_path):
                f = open(file_path, "w+")
                f.write("T [C], P [mbar]\n")
            else:
                f = open(file_path, "a")

            f.write(f"{data[0]}, {data[1]}\n")
            
            f.close()
            return
        case 2:
            if mode == None:
                file_path = os.path.join(data_folder, "calculator_adsorption_potential_results.csv")
                if not os.path.isfile(file_path):
                    f = open(file_path, "w+")
                    f.write("dF [J/mol], T_1 [C], T_2 [C], p [mbar], pp0 [-]\n")
                else:
                    f = open(file_path, "a")

                f.write(f"{data[0]}, {data[1]}, {data[2]}, {data[3]}, {data[4]}\n")
            
                f.close()
                return
            if mode == "cycle":
                file_path = os.path.join(data_folder, "calculator_adsorption_potential_cycle_results.csv")
                if not os.path.isfile(file_path):
                    f = open(file_path, "w+")
                    f.write("dF_high [J/mol], dF_low [J/mol], T_1 [C], T_2 [C], T_3 [C]\n")
                else:
                    f = open(file_path, "a")

                f.write(f"{data[0]}, {data[1]}, {data[2]}, {data[3]}, {data[4]}\n")
            
                f.close()
                return
            return