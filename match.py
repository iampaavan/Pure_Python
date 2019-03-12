import re

sentence = 'Start a sentence and then bring it to an end'

# pattern = re.compile(r'Start')

# pattern = re.compile(r'end')
# pattern = re.compile(r'abc')
# pattern = re.compile(r'start', re.IGNORECASE)
pattern = re.compile(r'start', re.I)
# matches = pattern.match(sentence) # to match the starting word of the String
matches = pattern.search(sentence) # to search only one word after the start
print(matches)
