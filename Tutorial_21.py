print()
list_1 = [9, 1, 8, 2, 7, 3, 6, 4, 5]
print('Original unsorted list: ', list_1)

print()
print('*************************************')
print()

sort_list_1 = sorted(list_1)
print('Sorted list using sorted method', sort_list_1)

print()
print('*************************************')
print()

list_1.sort()
print('Sorted the original List using sort(): ', list_1)

print()
print('*************************************')
print()

sort_list_2 = sorted(list_1, reverse=True)
print('Sorted the list in reverse order', sort_list_2)

print()
print('*************************************')
print()

list_1.sort(reverse=True)
print('Sorted the original List and reversed it, using sort(): ', list_1)

print()
print('*************************************')
print()

tup_1 = (9, 1, 8, 2, 7, 3, 6, 4, 5)
sort_tup_1 = sorted(tup_1, reverse=True)
print('Sorted the tup and reversed: ', sort_tup_1)

print()
print('*************************************')
print()

sort_tup_2 = sorted(tup_1, reverse=False)
print('Sorted the original tup: ', sort_tup_2)

print()
print('*************************************')
print()

my_dictionary = {'Name': 'Paavan', 'Age': 27, 'Job': 'Programming', 'OS': 'Windows'}
sorted_dic = sorted(my_dictionary)
print(sorted_dic)

print()
print('*************************************')
print()

list_2 = [-6, -5, -4, 1, 2, 3]
print('Original List_2', list_2)

print()
print('*************************************')
print()

sort_list_2 = sorted(list_2, key = abs)
print('Sorted the list based on absolute value: ', sort_list_2)

print()
print('*************************************')
print()
