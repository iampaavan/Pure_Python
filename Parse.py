import csv

html_list = ''
names = []

with open('C:\\Users\\Paavan Gopala\\Desktop\\OS-Demo\\New Folder\\patrions.csv') as data_file:
	csv_data = csv.DictReader(data_file)
	
	# ignore the header in the first line of bad data

	next(csv_data)
	
	for line in csv_data:
		if line['FirstName'] == 'No Reward':
			break
		names.append(f"{line['FirstName']} {line['LastName']}")

html_list += f'<p>There are currently {len(names)} public contributors. Thank You! </p>'

html_list += f'\n<ul>'

for name in names:
	html_list += f'\n\t<li>{name}</li>'

html_list += f'\n</ul>'

print(html_list)
