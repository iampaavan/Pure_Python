import collections
"""Write a Python program to sum of all counts in a collections."""


def count_collections():
	"""return sum of all counts"""
	num = [2, 2, 4, 6, 6, 8, 6, 10, 4]
	result = sum(collections.Counter(num).values())
	return result


print(f"Sum of all counts in a collection: {count_collections()}")
print(f'********************************************************')


def counter():
	"""return sum of all counts."""
	
	counter = 0
	
	num = [2, 2, 4, 6, 6, 8, 6, 10, 4]

	for i in range(1, len(num) + 1):
		counter += 1

	return counter


print(f"Sum of all counts in a collection: {counter()}")
