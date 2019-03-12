my_list = [1, 2, 3, 4, 5, 6]
print(len(my_list))

# LBYL (Non-Pythonic)
print()

if len(my_list) >= 6:
	print(my_list[5])

else:
	print('The index doesn\'t exist!!!')
	
print()
print('******************************************************')
print()

# EAFP (Pythonic)

try:
	print(my_list[6])
	
except IndexError as I:
	print(I)
