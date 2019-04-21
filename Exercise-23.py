"""Write a Python program to count the number 4 in a given list."""


def count_list_4(my_list):
	"""Return the how many times 4 is in the list."""
	count = 0
	
	for l in my_list:
		if l == 4:
			count += 1
			
	return count


print(f"The number '4' is repeated {count_list_4([1, 4, 6, 7, 4])} times.")
print(f'****************************************************************************')
print(f"The number '4' is repeated {count_list_4([1, 4, 6, 4, 7, 4])} times.")
