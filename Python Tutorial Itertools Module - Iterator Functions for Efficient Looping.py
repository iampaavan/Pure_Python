import itertools, operator

counter = itertools.count()
# print(next(counter))
# print(next(counter))

data = [100, 200, 300, 400]
# daily_data = list(zip(itertools.count(start=1), data))
daily_data = list(itertools.zip_longest(range(10), data))
print(daily_data)

cycle_counter_number = itertools.cycle([1, 2, 3])
cycle_counter_string = itertools.cycle(('On', 'Off'))

print(next(cycle_counter_string))
print(next(cycle_counter_string))
print(next(cycle_counter_string))
print(next(cycle_counter_string))
print(next(cycle_counter_string))
print(next(cycle_counter_string))

cycle_counter_repeat = itertools.repeat(2, times=5)
repeat_list = []

for i in cycle_counter_repeat:
    repeat_list.append(i)

print(repeat_list)

squares = list(map(pow, range(10), itertools.repeat(2)))
print(squares)

squares_starmap = list(itertools.starmap(pow, [(0, 2), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2)]))
print(squares_starmap)

letters = ['a', 'b', 'c', 'd', 'e']
numbers = [0, 1, 2, 3, 2, 1, 0]
names = ['Paavan', 'Bhushan']

result_combinations = list(itertools.combinations(letters, 2))
print(result_combinations)
print(len(result_combinations))

result_permutations = list(itertools.permutations(letters, 2))
print(result_permutations)
print(len(result_permutations))

password = list(itertools.product(numbers, repeat=4))
print(len(password))
print(password)

comb_with_repeat = list(itertools.combinations_with_replacement(numbers, 4))
print(len(comb_with_repeat))
print(comb_with_repeat)

combine = list(itertools.chain(letters, numbers, names))
print(combine)

result_islice = list(itertools.islice(range(10), 1, 5))
print(result_islice)

print(f'*******************************************************************')

with open('test_new.log') as f:
    header = itertools.islice(f, 3)

    for line in header:
        print(line, end='')

print(f'*******************************************************************')

test = ['a', 'b', 'c', 'd']
selectors = [True, True, False, True]

result_compress = list(itertools.compress(test, selectors))
print(result_compress)
print(f'*******************************************************************')


def less_than_2(numbers):
    if numbers < 2:
        return True
    return False


result_filter = list(filter(less_than_2, numbers))
print(result_filter)
print(f'*******************************************************************')

result_filter_false = list(itertools.filterfalse(less_than_2, numbers))
print(result_filter_false)
print(f'*******************************************************************')

result_drop_while = list(itertools.dropwhile(less_than_2, numbers))
print(result_drop_while)
print(f'*******************************************************************')

result_take_while = list(itertools.takewhile(less_than_2, numbers))
print(result_take_while)
print(f'*******************************************************************')

result_accumulate = list(itertools.accumulate(numbers))
print(result_accumulate)
print(f'*******************************************************************')

sample = [1, 2, 3, 4, 5, 6]
result_accumulate_product = list(itertools.accumulate(sample, operator.mul))
print(result_accumulate_product)
print(f'*******************************************************************')


def get_state(person):
    return person['state']


people = [
    {
        'name': 'John Doe',
        'city': 'Gotham',
        'state': 'NY'
    },
    {
        'name': 'Jane Doe',
        'city': 'Kings Landing',
        'state': 'NY'
    },
    {
        'name': 'Corey Schafer',
        'city': 'Boulder',
        'state': 'CO'
    },
    {
        'name': 'Al Einstein',
        'city': 'Denver',
        'state': 'CO'
    },
    {
        'name': 'John Henry',
        'city': 'Hinton',
        'state': 'WV'
    },
    {
        'name': 'Randy Moss',
        'city': 'Rand',
        'state': 'WV'
    },
    {
        'name': 'Nicole K',
        'city': 'Asheville',
        'state': 'NC'
    },
    {
        'name': 'Jim Doe',
        'city': 'Charlotte',
        'state': 'NC'
    },
    {
        'name': 'Jane Taylor',
        'city': 'Faketown',
        'state': 'NC'
    }
]

person_group = itertools.groupby(people, get_state)

for key, group in person_group:
    for person in group:
        print(person)
    print()
print(f'*******************************************************************')


person_group_count = itertools.groupby(people, get_state)
for k, g in person_group_count:
    print(k, len(list(g)))

print(f'*******************************************************************')

person_group_copy = itertools.groupby(people, get_state)
copy1, copy2 = itertools.tee(person_group_copy)

for i, j in copy1:
    for k in j:
        print(k)

print(f'*******************************************************************')
