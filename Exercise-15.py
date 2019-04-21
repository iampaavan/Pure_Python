from datetime import date
"""Write a Python program to calculate number of days between two dates."""
first_date = date(2014, 7, 2)
last_date = date(2014, 7, 11)
delta = last_date - first_date
print(f"First Date: {first_date}")
print(f"Second Date: {last_date}")
print(f'*****************************************************************')
print(f"Difference between the two dates are: {delta.days} days.")
print(f'*****************************************************************')

