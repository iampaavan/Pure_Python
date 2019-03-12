import csv

with open( 'C:\\Users\\Paavan Gopala\\Desktop\\OS-Demo\\New Folder\\names.csv', 'r' ) as csv_file:
	csv_reader = csv.reader( csv_file )
	
	# next(csv_reader)
	with open( 'C:\\Users\\Paavan Gopala\\Desktop\\OS-Demo\\New Folder\\new_names_1.csv', 'w' ) as new_file:
		csv_writer = csv.writer( new_file, delimiter='\t' )
		
		for lines in csv_reader:
			csv_writer.writerow( lines )

print('****************************************************************************************************s')


with open( 'C:\\Users\\Paavan Gopala\\Desktop\\OS-Demo\\New Folder\\names.csv', 'r' ) as csv_file:
	csv_reader = csv.DictReader( csv_file )
	next( csv_reader )
	for lines in csv_reader:
		print( lines['email'] )

print('****************************************************************************************************')


with open('C:\\Users\\Paavan Gopala\\Desktop\\OS-Demo\\New Folder\\names.csv', 'r') as csv_file:
	
	csv_reader = csv.DictReader(csv_file)
	
	with open('C:\\Users\\Paavan Gopala\\Desktop\\OS-Demo\\New Folder\\new_names_dict.csv', 'w') as new_file:
		
		field_names = ['first_name', 'last_name', 'email'] # remove 'email' field
		csv_writer = csv.DictWriter(new_file, fieldnames=field_names, delimiter="\t")
		
		csv_writer.writeheader()
		
		for lines in csv_reader:
			# del lines['email'] # email not needed, then insert this line
			csv_writer.writerow(lines)
