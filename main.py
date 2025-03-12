import os.path

from main_interface import run_the_interface


def main():
    #global file_path_df_curve 
    #global file_path_to

    # То что происходит дальше с путями - херня полная. 
    # Нужно переделать. Подавать в главный интерфейс название куда, откуда и название файла.
    # В ином случае в записи в файл сплошные костыли с этим... 
    file_path_from = "data"
    file_path_to = "calculated"
    df_curve_file = "w_vs_dF_B150_25CaCl2" #Change file here!
    os.makedirs(file_path_to, exist_ok=True)
    df_curve_ext = ".csv" #The code is working with .csv
    df_curve = df_curve_file + df_curve_ext
    file_path_df_curve = os.path.join(file_path_from, df_curve) #solving Linux vs Windows separator problem
    file_path_to_full = os.path.join(file_path_to, df_curve_file)
    
    print("Welcome to the sorption calculator. Available subroutines:")
    
    run_the_interface(file_path_df_curve, file_path_to_full)
    

main()
