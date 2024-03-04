# Write a Python program to check for access to a specified path. 
# Test the existence, readability, writability and executability of the specified path

import os

path = os.getcwd()

print(f"Existence: {os.access(path,os.F_OK)}")
print(f"Readability: {os.access(path,os.R_OK)}")
print(f"Writability: {os.access(path,os.W_OK)}")
print(f"Executability: {os.access(path,os.X_OK)}")