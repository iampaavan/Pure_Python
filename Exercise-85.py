from operator import itemgetter
"""Write a Python program to count the number occurrence of a specific character in a string."""

my = list()


def occurence(string):
	"""return the character occurence in a string."""
	
	l = list()
	
	for i in string:
		l.append(i)
		
	d = dict()
	
	for j in l:
		d[j] = d.get(j, 0) + 1
	
	for key, value in sorted(d.items(), key=itemgetter(1), reverse=False):
		my.append((key, value))
		
	print(my)
	

print(f'*****************************************************************')
occurence('ababsfgsdgsdgac')
print(f'*****************************************************************')

