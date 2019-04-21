import socket
"""Write a Python program to get the name of the host on which the routine is running."""


def hostname():
	"""return the hostname."""
	host_name = socket.gethostname()
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect(('8.8.8.8', 80))
	my_ip, port_number = s.getsockname()
	return host_name, my_ip, port_number


print(f"Hostname on which the routine is running: {hostname()[0]}")
print(f"My Local IP address: {hostname()[1]}")
print(f"Port Number: {hostname()[2]}")
