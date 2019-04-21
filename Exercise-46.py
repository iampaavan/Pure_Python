from subprocess import check_output
"""Write a python program to call an external command in Python"""
print(check_output("dir C:", shell=True).decode())
