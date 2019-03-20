for numbers in range(1, 101):

	if numbers % 5 == 0 and numbers % 3 == 0:
		print('FizzBuzz')
	elif numbers % 3 == 0:
		print('Fizz')
	elif numbers % 5 == 0:
		print('Buzz')
	else:
		print(numbers)

print()
print('******************************************')
print()

# Fibonacci Series

a, b = 0, 1
for i in range(1, 11):
	print(a)
	a, b = b, a + b
