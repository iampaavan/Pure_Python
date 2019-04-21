import os
"""Write a python program to get the path and name of the file that is currently executing."""
print(f'*************************************************************************************')
print(f"Current filename and its absolute path: {os.path.realpath(__file__)}")
print(f'*************************************************************************************')

