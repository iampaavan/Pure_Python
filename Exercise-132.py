"""Write a Python program to split a variable length string into variables."""
my_list = ['a', 'b', 'c']
my_list_1 = [1, 2]


def string_to_variable():
	"""string to variable."""
	x, y, z = (my_list + [None] * 3)[:3]
	a, b = (my_list_1 + [None] * 2)[:2]
	print(f"{x} {y} {z}")
	print(f"{a} {b}")


string_to_variable()
print(f'***********************************************')
l = list()


def s_to_v():
	for i in my_list:
		l.append(i)
		
	return l


print(f"{s_to_v()[0]} {s_to_v()[1]} {s_to_v()[2]}")


