import os.path

from main_interface import initiate_the_interface


def main():
    path_from = "data"
    path_to = "calculated"
    df_curve_file = "w_vs_dF_B150_25CaCl2" #Change file here!
    os.makedirs(path_to, exist_ok=True)
    df_curve_ext = ".csv" #The code is working with .csv
    
    initiate_the_interface(path_from, path_to, df_curve_file, df_curve_ext)
    

main()
