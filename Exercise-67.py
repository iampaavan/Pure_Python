import time, cProfile
"""Write a Python program to convert seconds to day, hour, minutes and seconds."""


def convert_seconds(seconds):
	"""return seconds in hours, minutes and seconds."""
	
	day = str(seconds / (24 * 3600)) + ' days'
	hour = str(seconds / 3600) + ' hours'
	minutes = str(seconds / 60) + ' minutes'
	sec = str(seconds) + ' seconds'
	return day, hour, minutes, sec


print(f'**********************************************')
print(f'Time in Days, Hours, Minutes, Seconds: {convert_seconds(86399)}')
print(f'**********************************************')
cProfile.run('convert_seconds(86399)')


def time_func(my_time):
	start_time = round(time.perf_counter(), 10)
	print(f"Function  start time: {start_time}")
	
	
	day = str(my_time // (24 * 3600)) + ' days'
	my_time %= (24 * 3600)
	hour = str(my_time // 3600) + ' hours'
	my_time %= 3600
	minute = str(my_time // 60) + ' minutes'
	my_time %= 60
	second = str(my_time) + ' seconds'
	
	end_time = time.perf_counter()
	finish = abs(end_time - start_time)
	print(f"Function end time: {finish}")
	return day, hour, minute, second


print(f'****************************************************')
print(f"Time: {time_func(86399)}")
print(f'****************************************************')
cProfile.run('time_func(86399)')


