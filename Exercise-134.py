from timeit import default_timer
import time
"""Write a Python program to calculate the time runs (difference between start and current time)of a program."""
l = list()

start = round(time.perf_counter(), 10)
print(f"Program Start Time: {start}")


def cal_time(number):
	"""display start and end time of the program."""
	
	for i in range(1, number):
		l.append(i)
		
	end_time = abs(time.perf_counter() - start)
	return round(end_time, 6)


print(f"End time of the program: {cal_time(100000)}")
print(f'*******************************************')
k = list()


def time_calc(num):
	"""return execution time."""
	pgm_start = default_timer()
	print(f"Program Start Time: {pgm_start}")
	
	for j in range(1, num):
		k.append(j)
		
	pgm_end = round(abs(default_timer() - pgm_start), 6)
	
	return pgm_end


print(f"Program Execution End Time: {time_calc(100000)}")
