"""Write a Python program which accepts a sequence of comma-separated numbers from user and generate a
list and a tuple with those numbers"""

sequence_numbers = input(f"Enter the sequence of numbers: ")
value = sequence_numbers.split(',')
print(value)
print(f'**************************************************')
print(f"List of numbers: {list(value)}")
print(f'**************************************************')
print(f'Tuple of numbers: {tuple(value)}')
print(f'**************************************************')
