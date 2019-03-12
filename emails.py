import re

emails = '''
PaavanGopala@gmail.com
paavan.gopala@northeastern.edu
paavan-007-gopala@my-work.net
'''

# pattern = re.compile(r'[a-zA-Z0-9.-]+@[a-z-A-Z]+\.(com|edu|net)')
pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')

matches = pattern.finditer(emails)

for match in matches:
	print(match)
