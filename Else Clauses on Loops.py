my_list = [1, 2, 3, 4, 5]
for i in my_list:
	print(i)
else:
	print('Hit the For\Else Statement')


print()
print('********************************')
print()

j = 1
while j <= 5:
	print(j)
	j += 1
	if j == 3:
		break
else:
	print('Hi the While\Else Statement')

print()
print('********************************')
print()


def find_index(to_search, target):
	
	for i, value in enumerate(to_search):
		if value == target:
			break
	else:
		return -1
	return i


my_list_1 = ['Manju', 'Thilak', 'Suu', 'Sharu', 'Paavan']
index_value = find_index(my_list_1, 'Paavan')
print(f'Location of the target is at index "{index_value}"')
print()
print('************************************************')
print()

lists = ['ABC', 'BCD', 'CDE', 'EFG']
print(f'Index of "BCD" found at: {lists.index("BCD")}')
print()


def index_to_search(index_search, value_target):
	
	for index, values in enumerate(index_search):
		if values == value_target:
			break
	else:
		return -1
	
	return index


search = index_to_search(lists, 'BCD')
print(f'Location found at index: {search}')
