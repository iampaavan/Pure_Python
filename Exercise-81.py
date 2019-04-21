import sys
"""Write a Python program to get the current value of the recursion limit."""


def get_recursion_limit():
	""":return current recursion limit."""
	print(f'*****************************************************************')
	print(f"Current System Recursion Limit: {sys.getrecursionlimit()}")
	print(f'*****************************************************************')
	

get_recursion_limit()