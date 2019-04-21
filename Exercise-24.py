"""Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string.
Return the n copies of the whole string if the length is less than 2."""


def count_string(string, count):
	
	result = ''
	
	for i in range(count):
		
		if len(string) < 2:
			result = result + string
	
		else:
			for j in string[:2]:
				result = result + j
				
	return result
	
		
print(count_string('abcd', 3))
print(f'*****************************************************')
print(count_string('a', 5))
print(f'*****************************************************')
