import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
paavan.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

cat
mat
pat
bat

'''

sentence = 'Start a sentence and then bring it to an end'

# pattern = re.compile(r'abc')
# pattern = re.compile(r'\.')
# pattern = re.compile(r'paavan\.com')
# pattern = re.compile(r'\d')
# pattern = re.compile(r'\D')
# pattern = re.compile(r'\BHa')
# pattern = re.compile(r'^Start')
# pattern = re.compile(r'end$')
# pattern = re.compile(r'\d\d\d[.]\d\d\d[.]\d\d\d\d')
# pattern = re.compile(r'[89]00[-]\d\d\d[-]\d\d\d\d')
# pattern = re.compile(r'[1-5]')
# pattern = re.compile(r'[a-zA-Z]')
# pattern = re.compile(r'[^a-zA-Z]')
# pattern = re.compile(r'[^b]at')
# pattern = re.compile(r'\d{3}.\d{3}.\d{4}')
# pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*')
pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*')
# pattern = re.compile(r'\d{3}.\d{3}.\d{4}')
# pattern = re.compile(r'Start')
# matches = pattern.findall(text_to_search)
matches = pattern.finditer(text_to_search)
# matches = pattern.match(sentence)

for match in matches:
	print(match)

print()
print('**************************************************')

with open('data.txt', 'r') as f:
	
	contents = f.read()
	# pattern = re.compile(r'\d\d\d[-]\d\d\d[-]\d\d\d\d')
	# pattern = re.compile(r'[89]00[-]\d\d\d[-]\d\d\d\d')
	pattern = re.compile(r'[89]00[-]\d{3}[-]\d{4}')
	matches = pattern.finditer(contents)
	
	# print(matches)

	for match in matches:
		print(match)

# print(text_to_search[1:4])