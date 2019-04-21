import json
"""Write a Python program to use double quotes to display strings."""
my_list = ['ones', 'threes', 'ones', 'ones', 'twos', 'threes', 'twos', 'fours', 'fours', 'fours', 'fours']
d = dict()


def double_quotes():
	"""return strings in double quotes"""
	for i in my_list:
		d[i] = d.get(i, 0) + 1
	
	print(f"My Original Dictionary: {d}")
	my_json = json.dumps(d)
		
	return my_json


print(f"My Dictionary: {double_quotes()}")

