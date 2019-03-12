nums = [1, 2, 3, 4, 5]

for num in nums:
	print(num)

print(sum(nums))

for index, numb in enumerate(nums):
	print('Index', index, 'has the element', '--> ',  numb)

print()

test = [1, 3, 5, 7, 9]

for odd in test:
	if odd == 3:
		print('Found the element')
		break
	
	print(odd)

print()

for odd in test:
	if odd == 3:
		print('Found the element')
		continue
	
	print(odd)

print()

for odd in test:
	for letter in 'abc':
		print(odd, letter)

for i in range(10):
	print(i)

for j in range(1, 11):
	print(j)

x = 0

while x <= 10:
	print(x)
	x += 1

print()

y = 0
while y <= 10:
	if y == 5:
		break
	print(y)
	y += 1

print()

z = 0
while True:
	if z == 7:
		break
	print(z)
	z += 1




