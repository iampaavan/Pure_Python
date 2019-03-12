from my_module import find_index, test
import sys
import random
import math
import datetime
import calendar
import os
# import antigravity


courses = ['Data Networks', 'Java', 'Connected Devices', 'Cloud Computing']

index = find_index(courses, 'Java')

print('Index value of the target element is: ', index)
print(test)

print(sys.path)

course_random = random.choice(courses)
print(course_random)

radian = math.radians(90)
print(radian)
print(math.sin(radian))


today = datetime.date.today()
print('Today\'s date is: ', today)

print('Is 2020 a Leap Year?: ', calendar.isleap(2020))
print('Is 2017 a Leap Year?: ', calendar.isleap(2017))

print(os.getcwd())
print(os.__file__)
