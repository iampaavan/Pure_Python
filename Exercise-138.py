"""Write a Python program to extract single key-value pair of a dictionary in variables."""
d = {'Paavan': 14, 'Manju': 21, 'Thilak': 29}
l = list()


def extract():
	"""return only a single key-value pair."""
	for key, value in d.items():
		l.append((key, value))
		
	return l


print(f"Key_Value pair: {extract()[0]}")
