import multiprocessing, os
"""Write a Python program to find out the number of CPUs using."""
print(f'*********************************************************')
print(f'CPU Count using OS module: {os.cpu_count()} CPU\'s')
print(f'*********************************************************')
print(f"CPU Count Info using multiprocessing module: {multiprocessing.cpu_count()} CPU's")
print(f'*********************************************************')
