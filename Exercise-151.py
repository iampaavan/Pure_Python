"""Write a Python function to find a distinct pair of numbers whose product is odd
from a sequence of integer values."""


def find_odd_product(my_list):
	"""return boolean based on odd product value"""
	
	for i in range(len(my_list)):
		
		for j in range(len(my_list)):
			
			if i != j:
				product = my_list[i] * my_list[j]
				print(product)
				
				if product & 1:
					
					return True
					

print(f"List has odd products?: {find_odd_product([1, 6, 4, 7, 8])}")
print(f'***********************************************************')
print(f"List has odd products?: {find_odd_product([6, 4, 7, 8])}")
