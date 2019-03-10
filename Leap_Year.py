# Number of days in a month. First value is 0 used as a placeholder for indexing purpose
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(year):
	"""returns true for a leap year, else returns false"""
	return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):

	if not 1 <= month <= 12:
		return 'Invalid Month'
	
	if month == 2 and is_leap(year):
		return 29
	
	return month_days[month]


user_year = int(input('Enter the year: '))
user_month = int(input('Enter the month: '))
print('Number of days in the month is: ', days_in_month(user_year, user_month))

