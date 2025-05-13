# -*- coding: utf-8 -*-
"""
MultiDriveMapper

Created on Sat Apr 30 15:34:20 2022

@author: wardc

currently not designed as a single run script...but works reasonably well
if run interactively in spyder, idlex, ...


"""


import os
import pandas

#%%

drivename = input('name for the drive to map contents of\n:')
drivepath = input('path to drive to map contents of\n:')
outputfile = input('path to file to place results\n:')


#%%

print(f'starting content mapping of {drivename} : {drivepath}')

walked_drive = os.walk(drivepath)

errorlist=[]
with open(outputfile,'a+') as out_file:

    for r,d,f in walked_drive:
        for i in f:
            try:
                out_file.write(f'{drivename}\t{r}\t{os.path.join(r,i)}\t{i}\n')
            except:
                errorlist.append((r,i))
                print('unmappable file error')
print(f'finished content mapping of {drivename} : {drivepath}')


#%%

path_to_search_list = input('path to file with list of things to search for\n:')

path_to_walked_files = input('path to file with walked files\n:')

#%%

df_search_list = pandas.read_csv(path_to_search_list,sep='\t',header=None,names=['filename'])
df_walked_list = pandas.read_csv(path_to_walked_files,sep='\t',header=None,names=['drive','root','path','filename'],encoding='ISO-8859-1')

df_match = df_search_list.merge(df_walked_list, on='filename')
