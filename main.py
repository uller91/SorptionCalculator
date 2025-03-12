import os.path

from main_interface import run_the_interface


def main():
    #global file_path_df_curve 
    #global file_path_to
    file_path_from = "data"
    df_curve_file = "w_vs_dF_B150_25CaCl2" #Change file here!
    df_curve_ext = ".csv" #The code is working with .csv files
    df_curve = df_curve_file + df_curve_ext
    file_path_df_curve = os.path.join(file_path_from, df_curve) #solving Linux vs Windows separator problem
    file_path_to = os.path.join("calculated", df_curve_file)
    
    print("Welcome to the sorption calculator. Available subroutines:")
    
    run_the_interface(file_path_df_curve, file_path_to)
    

main()
