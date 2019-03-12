import csv

html_list = ''
names = []

with open('C:\\Users\\Paavan Gopala\\Desktop\\OS-Demo\\New Folder\\patrions.csv') as data_file:
	csv_data = csv.reader(data_file)
	
	# ignore the header's or first 2 lines of bad data
	next(csv_data)
	next(csv_data)
	
	for line in csv_data:
		if line[0] == 'No Reward':
			break
		names.append(f"{line[0]} {line[1]}")
		# print(names)
	# print(list(csv_data))

for name in names:
	print(name)

print()

html_list += f'<p>There are currently {len(names)} public contributors. Thank You! </p>'

# print(html_list)

print('\n')

html_list += f'\n<ul>'

for name in names:
	html_list += f'\n\t<li>{name}</li>'

html_list += f'\n</ul>'
print(html_list)

