import pandas as pd
import os

def name_change(sorted_list):
    """ This method will change image names
        adding numbers at the beggining """
    
    sorted_df = pd.DataFrame(sorted_list)
    
    # Find the largest number to find its digit
    max_num = sorted_df.loc[:, 1].max()

    # Find the digit of the largest number
    max_digit = len(str(max_num))
    
    # Format the numberings
    sorted_df[1] = sorted_df[1].apply(lambda x: f"[{x:0{max_digit}d}]")

    inc_indx = 0
    while inc_indx < len(sorted_df):
        temp_name = str(sorted_df.loc[inc_indx, 1]) + sorted_df.loc[inc_indx, 0]
        os.rename(sorted_df.loc[inc_indx, 0], temp_name)
        inc_indx += 1 