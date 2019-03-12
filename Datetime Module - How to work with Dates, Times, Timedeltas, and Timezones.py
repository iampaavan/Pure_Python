import datetime
import pytz

print()
my_date = datetime.date(1991, 7, 21)
sentence_13 = '{:%B %d, %Y}'.format(my_date)
print('My Bestie\'s Birthdate is: ', sentence_13)

print()
print('*******************************************')
print()

today_date = datetime.date.today()
print('Today\'s Date is: ', today_date)

print()
print('*******************************************')
print()

print(today_date.weekday())
print(today_date.isoweekday())

print()
print('*******************************************')
print()

time_delta = datetime.timedelta(days=7)
print('Date, next week from now is: ', today_date + time_delta)

print()
print('*******************************************')
print()

print('Date, previous week from today is: ', today_date - time_delta)

print()
print('*******************************************')
print()

my_birth = datetime.date(2019, 5, 14)
till_bday = my_birth - today_date
print('Time Duration to my birthday: ', str(till_bday.days) + ' days')

print()
print('*******************************************')
print()

print('Time Duration to my birthday: ', str(till_bday.total_seconds().__round__()) + ' seconds')

print()
print('*******************************************')
print()

t = datetime.time(9, 30, 45, 10000)
print(t)
print(t.hour)

print()
print('*******************************************')
print()

t_1 = datetime.datetime(2016, 5, 14, 15, 30, 45)
print(t_1)
print('Some Year\'s Date: ', t_1.date())
print('Today\'s Date and Time: ', t_1.today())
print('Some Year\'s Time: ', t_1.time())

print()
print('*******************************************')
print()

t_2 = datetime.datetime(2018, 10, 20, 18, 30, 5)
print('Some year\'s current date: ', t_2)
time_delta_1 = datetime.timedelta(days=7)
print('Some year\'s future date of 2018: ', t_2.date() + time_delta_1)
time_delta_2 = datetime.timedelta(hours=5)
print('Some year\'s future time is: ', t_2 + time_delta_2)

print()
print('*******************************************')
print()

t_3 = datetime.datetime.today()
t_4 = datetime.datetime.now()
t_5 = datetime.datetime.utcnow()

print(t_3)
print(t_4)
print(t_5)
print('Difference between current time and UTC current time: ', t_5 - t_3)

print()
print('*******************************************')
print()

t_6 = datetime.datetime(2019, 3, 10, 21, 20, 45, tzinfo=pytz.utc)
print(t_6)

t_7 = datetime.datetime.now(tz=pytz.utc)
print(t_7)

date_utc_now = datetime.datetime.utcnow().replace(tzinfo=pytz.utc)
print(date_utc_now)

print()
print('*******************************************')
print()

date_utc_now = datetime.datetime.utcnow().replace(tzinfo=pytz.utc)
print(date_utc_now)
date_eastern = date_utc_now.astimezone(pytz.timezone('US/Eastern'))
date_asian = date_utc_now.astimezone(pytz.timezone('Asia/Calcutta'))
print(date_eastern)
print(date_asian)

print()
print('*******************************************')
print()

for tz in pytz.all_timezones:
	print(tz)
	
print()
print('*******************************************')
print()

utc_time = datetime.datetime.now(tz=pytz.utc)
print(utc_time)

local_time = datetime.datetime.now()
print(local_time)
time_eastern = pytz.timezone('US/Eastern')
local_time = time_eastern.localize(local_time)
print(local_time)
my_time = utc_time.astimezone(pytz.timezone('US/Eastern'))
print(my_time)


print()
print('*******************************************')
print()

local_time_1 = datetime.datetime.now(tz=pytz.timezone('US/Eastern'))
print(local_time_1)
print(local_time_1.isoformat())
print(local_time_1.strftime('%B %d, %Y'))

print()
print('*******************************************')
print()

dt_str = 'March 10, 2019'
dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')
print(dt)

# strftime --> Datetime to String
# strptime --> String to Datetime

