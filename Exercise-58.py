import time
"""Write a program to get execution time (in seconds) for a Python method."""


def sum_n_times(number):
	sum = 0
	try:
		start_time = round(time.perf_counter(), 10)
	
	except DeprecationWarning:
		pass
	
	else:
		print(f"Start Time of the Funtion: {start_time}")
		for i in range(number + 1):
			sum += i
		
		end_time = time.perf_counter()
		finish = abs(end_time - start_time)
		return sum, finish


print(f"Sum of first 5 integers and End Time is: {sum_n_times(8)}")
