# Python program to sum the given series
# Returns sum of n + nn + nnn + .... (m times)


def Series(n, m):
	# Converting the number to string
	str_n = str(n)
	
	# Initializing result as number and string
	sums = n
	sum_str = str(n)
	
	# Adding remaining terms
	for i in range(1, m):
		# Concatenating the string making n, nn, nnn...
		sum_str = sum_str + str_n
		
		# Before adding converting back to integer
		sums = sums + int(sum_str)
	
	return sums


# Driver Code

total = Series(5, 3)
print(total)
