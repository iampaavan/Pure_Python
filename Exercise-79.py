import sys, textwrap, cProfile
"""Write a Python program to find the available built-in modules."""


def check_built_in():
	modules = ', '.join(sorted(sys.builtin_module_names))
	print(textwrap.fill(modules, width=100))


print()
cProfile.run('check_built_in()')
