# Write a Python program to list only directories, files and all directories, files in a specified path.

import os

folder_name = input()
path = f"../{folder_name}/"

dirs_list = os.listdir(path)

print("directories:")
for dir in dirs_list:
    if os.path.isdir(dir):
        print(dir)
        
print("files:")
for dir in dirs_list:
    if os.path.isfile(dir):
        print(dir)