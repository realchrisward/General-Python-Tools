# -*- coding: utf-8 -*-
"""
File Denesting Tool

@author: wardc
"""

#%% import libraries
from PyQt5.QtWidgets import QApplication, QListView, QInputDialog
from PyQt5.QtWidgets import QFileDialog, QAbstractItemView, QTreeView
import sys
import os
import shutil

#%% select folders to search
app = QApplication(sys.argv)

file_dialog = QFileDialog()
file_dialog.setFileMode(QFileDialog.DirectoryOnly)
file_dialog.setOption(QFileDialog.DontUseNativeDialog, True)
file_view = file_dialog.findChild(QListView, 'listView')

# to make it possible to select multiple directories:
if file_view:
    file_view.setSelectionMode(QAbstractItemView.MultiSelection)
f_tree_view = file_dialog.findChild(QTreeView)
if f_tree_view:
    f_tree_view.setSelectionMode(QAbstractItemView.MultiSelection)

if file_dialog.exec():
    selected_paths = file_dialog.selectedFiles()

input_paths = []
for i in range(len(selected_paths)-1):
    if selected_paths[i] in selected_paths[i+1]:
        pass
    else:
        input_paths.append(selected_paths[i])
input_paths.append(selected_paths[-1])
    
print('Directories to Search')
for i in input_paths:
    print(i)

#%% select output location

output_path = QFileDialog.getExistingDirectory(
    None,
    'Select Output Location'
    'Select Output Location',
    )
print(f'\nOutput Location\n{output_path}')
#%% select filetypes to copy
extension_text = QInputDialog.getText(
    None,'Extensions to copy','Extensions to copy', text = '.jpg'
    )[0]
print(f'\nExtensions to copy: {extension_text}')
#%% crawl the directory to get filepaths
file_list = []

for folder in input_paths:
    found_files = os.walk(folder)
    for d,p,f in found_files:
        for filename in f:
            if os.path.splitext(filename)[1] == extension_text:
                file_list.append(os.path.join(d,filename))

#%% copy the files to the output directory
print(f'{len(file_list)} files to copy...')
counter = 0
rounded_status = 0
for f in file_list:
    counter += 1
    if counter/len(file_list) * 100 >= rounded_status +1:
        rounded_status = int(counter/len(file_list)*100)
        print(f'{rounded_status} %')
    shutil.copy2(f,output_path)
print('all done')

input('press ENTER to close')