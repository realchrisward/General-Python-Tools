# -*- coding: utf-8 -*-
"""
concat_csv_files

@author: wardc
"""
__version__ = "1.0.0"

# %% import libraries
import os
import pandas


# %% define main
def main():
    # %%
    input_dir = input("path to folder with csv files")
    output_path = input("filename for concatenated output")

    # %%
    file_list = [
        os.path.join(input_dir, f)
        for f in os.listdir(input_dir)
        if os.path.isfile(os.path.join(input_dir, f))
    ]

    df_list = []

    for file in file_list:
        print(f"grabbing data from: {file}")
        df_list.append(pandas.read_csv(file))
    # %%
    df = pandas.concat(df_list)

    df.to_csv(output_path)
    print("all done")
    # %%


if __name__ == "__main__":
    main()
