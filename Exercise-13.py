import calendar
"""Write a Python program to print the calendar of a given month and year."""

y = int(input(f"Enter the year: "))
m = int(input(f"Enter the month: "))
month = calendar.month(y, m)
print(f"Year and Month:{month}")
c = calendar.monthrange(2019, 4)
print(c)
