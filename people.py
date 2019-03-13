import mem_profile
import random
import time

names = ['John', 'Corey', 'Adam', 'Steve', 'Rick', 'Thomas']
majors = ['Math', 'Engineering', 'CompSci', 'Arts', 'Business']

print()
print('Memory (Before): {}Mb'.format(mem_profile.memory_usage_psutil()))


def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
                    'id': i,
                    'name': random.choice(names),
                    'major': random.choice(majors)
                }
        result.append(person)
    return result


def people_generator(num_people):
    for i in range(num_people):
        person = {
                    'id': i,
                    'name': random.choice(names),
                    'major': random.choice(majors)
                }
        yield person


t1 = time.process_time()
print(f'{t1:.20f}')
people = people_list(10000000)
t2 = time.process_time()
print(f'{t2:.20f}')

print('Memory (After) : {}Mb'.format(mem_profile.memory_usage_psutil()))
print('Took {} Seconds'.format(t2-t1))

print()
print('****************************************************')
print()


t3 = time.process_time()
print(f'{t3:.20f}')
people = people_generator(10000000)
t4 = time.process_time()
print(f'{t3:.20f}')

print('Memory (After) : {}Mb'.format(mem_profile.memory_usage_psutil()))
print('Took {} Seconds'.format(t4-t3))

