"""Write a Python program to print all even numbers from a given numbers list in the same order and stop
the printing if any numbers that come after 237 in the sequence."""


def print_even_numbers(my_list):
	"""Return even numbers upto 237."""
	l = list()
	for i in my_list:
		if i % 2 == 0 and i > 237:
			l.append(i)
			
	return l


even = print_even_numbers([386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958,743, 527])
print(f"list of even numbers greater than 237: {even}")

