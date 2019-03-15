import datetime
import calendar

balance = 86000
interest_rate = 24 * 0.01
monthly_payment = 8600

today = datetime.date.today()
print(type(today))
print("Today's date --> ", today)
print("Today's date with only the date --> ", today.day)
print()

days_in_current_month = calendar.monthrange(today.year, today.month)
print("Current day of the week and total days in the current month --> ", days_in_current_month)
print()

days_in_current_month_only = calendar.monthrange(today.year, today.month)[1]
#print(type(calendar.monthrange(today.year, today.month)))
print("Total number of days in the current month --> ", days_in_current_month_only)
print()

days_in_current_month_left = days_in_current_month_only - today.day
print("Number of days left until 1st day of next month --> ", days_in_current_month_left)
print()

bill_payment_start_date = today + datetime.timedelta(days=days_in_current_month_left + 1)
print("Bill payment start date: ", bill_payment_start_date)
print()

bill_payment_end_date = bill_payment_start_date

while balance > 0:
	interest_charge = (interest_rate / 12) * balance
	balance += interest_charge
	balance -= monthly_payment
	
	balance = round(balance, 2)
	
	if balance < 0:
		balance = 0
		
	# balance = 0 if balance < 0 else round(balance, 2)
	
	print("Payment Date is:", bill_payment_end_date, "and Balance =", balance)
	days_in_current_month_only = calendar.monthrange(bill_payment_end_date.year, bill_payment_end_date.month)[1]
	bill_payment_end_date = bill_payment_end_date + datetime.timedelta(days=days_in_current_month_only)