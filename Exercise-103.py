import subprocess
"""Write a Python program to get system command output."""


def command_output():
	"""return command output"""
	my_output = subprocess.check_output("dir", shell=True, universal_newlines=True)
	return my_output


print(f"Command Output: {command_output()}")
