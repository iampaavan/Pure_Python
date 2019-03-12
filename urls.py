import re

urls = '''
https://www.google.com
http://paavangopala.com
https://youtube.com
https://www.nasa.gov
'''

# pattern = re.compile(r'https?://(www\.)?\w+\.(com|gov)')
pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')


subbed_urls = pattern.sub(r'\1\2\3', urls)
# subbed_urls = pattern.sub(r'\2\3', urls)

print(subbed_urls)

matches = pattern.finditer(urls)

for match in matches:
    print(match)
	# print(match.group(0))
	# print(match.group(1))
	# print(match.group(2))
	# print(match.group(3))


