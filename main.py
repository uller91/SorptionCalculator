import os.path

from main_interface import run_the_interface


def main():
    #global file_path_df_curve 
    #global file_path_to
    file_path_from = "data"
    df_curve = "w_vs_dF_B300_35CaCl2.csv"
    file_path_df_curve = os.path.join(file_path_from, df_curve) #solving Linux vs Windows separator problem
    file_path_to = "calculated"
    
    print("Welcome to the sorption calculator. Available subroutines:")
    
    run_the_interface(file_path_df_curve, file_path_to)
    

main()
