"""Write a Python program to convert all units of time into seconds."""


def time_conversion():
	"""return time in seconds"""
	days = int(input(f"Enter the number of days:")) * 3600 * 24
	hours = int(input(f"Enter the number of hours:")) * 3600
	minutes = int(input(f"Enter the number of minutes:")) * 60
	seconds = int(input(f"Enter the number of seconds:"))
	time = days + hours + minutes + seconds
	return time


print(f'****************************************')
print(f"Total Time: {time_conversion()} seconds.")
print(f'****************************************')
