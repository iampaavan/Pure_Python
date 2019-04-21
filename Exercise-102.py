from http.client import HTTPConnection
"""Write a Python program to access and print a URL's content to the console."""


def url_content():
	"""return the contents of the URL"""
	conn = HTTPConnection('www.google.com')
	conn.request('GET', '/')
	result = conn.getresponse()
	contents = result.read()
	return contents


print(f"Contents of the URL is as follows: {url_content()}")
