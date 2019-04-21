from os import walk
import os
"""Write a Python program to list all files in a directory in Python."""

mypath = os.getcwd()

f = []
for filenames in walk(mypath):
    f.append(filenames)
    
print(f)