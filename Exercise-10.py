"""Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn."""
number = int(input(f"Enter the number: "))
temp = str(number)
t1 = temp + temp
t2 = temp + temp + temp
result = number + int(t1) + int(t2)
print(f"Result: {result}")

print(f'**************************************************')


def compute():
	number = int(input(f"Enter the number: "))
	temp = str(number)
	t1 = temp + temp
	t2 = temp + temp + temp
	result = number + int(t1) + int(t2)
	print(f"Result: {result}")
	
	
compute()