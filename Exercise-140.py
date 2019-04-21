import socket
"""Write a Python program to valid an IP address."""


def valid_ip():
	"""check whether entered ip is valid or not."""
	ip = input('Enter your IP Address:')
	try:
		socket.inet_aton(ip)
		
	except socket.error:
		print(f"It's an invalid IP address.")
		
	else:
		print(f"It's a valid IP address.")
		
		
valid_ip()

