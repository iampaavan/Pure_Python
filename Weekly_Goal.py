import datetime

current_weight = 220
goal_weight = 180
average_lbs_week = 1.5

start_date = datetime.date.today()
print('Today\'s Date is: {:%B %d, %Y}'.format(start_date))

end_date = start_date
# print(end_date)

while current_weight > goal_weight:
	end_date += datetime.timedelta(days=7)
	current_weight -= average_lbs_week
	
print()
print('Date to reach the goal is: {:%B %d, %Y}'.format(end_date))
print()
print(f'Reached the goal in {(end_date - start_date).days // 7} weeks')

