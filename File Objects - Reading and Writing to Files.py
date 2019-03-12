# File Objects

import os

print( os.getcwd() )
os.chdir( 'C:\\Users\\Paavan Gopala\\Desktop\\OS-Demo\\New Folder' )
print( os.getcwd() )
f = open( 'C:\\Users\\Paavan Gopala\\Desktop\\OS-Demo\\New Folder\\test.txt' )

print( f.read() )
print( f.name )
print( f.mode )
f.close()

print()
print( '*****************************************' )
print()

with open( 'C:\\Users\\Paavan Gopala\\Desktop\\OS-Demo\\New Folder\\demo.txt' ) as h:
	h_contents = h.readline()
	print( h_contents, end='' )
	
	h_contents = h.readline()
	print( h_contents, end='' )

print()
print( f.closed )

print()
print( '*****************************************' )
print()

with open( 'C:\\Users\\Paavan Gopala\\Desktop\\OS-Demo\\New Folder\\sampleFICT.txt' ) as a:
	for index, line in enumerate( a ):
		print( index, line, end='' )

print()

print()
print( '*****************************************' )
print()

with open( 'C:\\Users\\Paavan Gopala\\Desktop\\OS-Demo\\New Folder\\sampleFICT.txt' ) as b:
	file_contents = b.read( 100 )
	print( file_contents )
	
	file_contents = b.read( 100 )
	print( file_contents )

print()
print( '*****************************************' )
print()

with open( 'C:\\Users\\Paavan Gopala\\Desktop\\OS-Demo\\New Folder\\sample.txt', 'r' ) as c:
	size_to_read = 10
	file_contents_c = c.read( size_to_read )
	
	while len( file_contents_c ) > 0:
		print( file_contents_c, end='*' )
		file_contents_c = c.read( size_to_read )
	
	size_to_read = 10
	
	file_contents_c = c.read( size_to_read )
	print( file_contents_c, end='' )
	
	# print(c.tell())
	c.seek( 0 )
	print()
	
	file_contents_c = c.read( size_to_read )
	print( file_contents_c )

with open( 'C:\\Users\\Paavan Gopala\\Desktop\\OS-Demo\\New Folder\\test.txt', 'r' ) as rf:
	with open( 'C:\\Users\\Paavan Gopala\\Desktop\\OS-Demo\\New Folder\\test _2.txt', 'w' ) as wf:
		for line in rf:
			wf.write( line )

with open( 'C:\\Users\\Paavan Gopala\\Desktop\\OS-Demo\\New Folder\\R2.jpg', 'rb' ) as rf:
	with open( 'C:\\Users\\Paavan Gopala\\Desktop\\OS-Demo\\New Folder\\R2 _2.jpg', 'wb' ) as wf:
		for line in rf:
			wf.write( line )

with open( 'C:\\Users\\Paavan Gopala\\Desktop\\OS-Demo\\New Folder\\sample.txt', 'r' ) as rf:
	with open( 'C:\\Users\\Paavan Gopala\\Desktop\\OS-Demo\\New Folder\\sample _2.txt', 'w' ) as wf:
		for line in rf:
			wf.write( line )

with open( 'C:\\Users\\Paavan Gopala\\Desktop\\OS-Demo\\New Folder\\R2.jpg', 'rb' ) as rf:
	with open( 'C:\\Users\\Paavan Gopala\\Desktop\\OS-Demo\\New Folder\\R2.jpg_3.jpg', 'wb' ) as wf:
		rf_chunk = 4096
		rf_read = rf.read( rf_chunk )
		
		while len( rf_read ) > 0:
			wf.write( rf_read )
			rf_read = rf.read( rf_chunk )
		



