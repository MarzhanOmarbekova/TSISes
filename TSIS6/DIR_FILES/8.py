# Write a Python program to delete file by specified path. 
# Before deleting check for access and whether a given path exists or not.

import os
path = "del"
if os.access(path,os.F_OK):
    os.rmdir(path)
