"""Write a Python program to display a floating number in specified numbers."""
my_list = [120, 5, 89, 64]
float_list = []


def conv_to_float():
	""":return float"""
	for i in my_list:
		float_list.append(round(float(i), 3))
		
	return float_list


print(f"Float numbers in list: {conv_to_float()}")
