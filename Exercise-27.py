"""Write a Python program to create a histogram from a given list of integers."""


def histogram(my_list):
	"""print a histogram."""
	
	for n in my_list:
		output = ''
		times = n
		
		while times > 0:
			output += '*'
			times -= 1
		
		print(output)
			

histogram([6, 5, 2, 1, 4])
