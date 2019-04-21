import traceback
"""Write a Python program to print the current call stack."""


def f1():
	return abc()


def abc():
	traceback.print_stack()
	
f1()