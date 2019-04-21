import datetime
"""Write a Python program to display the current date and time."""

today = datetime.datetime.today()

my_date = today.strftime("%Y-%m-%d %H:%M:%S")

print(f'*********************************************************')
print(f"Today's Date and Time is: {my_date}")
print(f'*********************************************************')

