import datetime
import math

goal_subs = 100000
current_subs = 85000
subs_to_go = goal_subs - current_subs
avg_subs_per_day = 200

days_to_go = math.ceil(subs_to_go / avg_subs_per_day)

today = datetime.date.today()

print()
print('Days to reach the goal is: ', today + datetime.timedelta(days=days_to_go))

