message_1 = 'Hello World'

message_2 = "Paavan's Lab"

message_3 = """Hey there how is your
day going on?"""

# print message_1 contents
print(message_1)

# print message_2 contents
print(message_2)

# print message_3 contents
print(len(message_3))

# print character at index 0
print(message_1[0])

# print the characters from index 0 inclusive upto index 5 exclusive
print(message_1[0:5])

# print the characters from index 0 inclusive upto index 5 exclusive
print(message_1[:5])

# print the characters from index 6 till the end of the string
print(message_1[6:])

# convert the string to lower case and print
print(message_1.lower())

# convert the string to upper case and print
print(message_1.upper())

# count how many times "Hello" appears in the string and print
print(message_1.count('Hello'))

# count how many times the character 'l' is present in the string and print
print(message_1.count('l'))

# returns index where 'World' starts and print
print(message_1.find('World'))

# if the character is not present, returns -1
print(message_1.find('Boss'))

# replace the character "World" with "Universe"
message_1 = message_1.replace("World", "Universe")

print(message_1)

greeting = 'Hello'
name = 'Paavan'

# message = greeting + ", " + name + ". Welcome!!!"
# message = '{}, {}. Welcome!!!'.format(greeting, name)
message = f'{greeting}, {name.upper()}. Welcome!!!'
print(message)

# get all the methods applicable for the string 'message'
print(dir(message))

# get more information of all the string methods
print(help(str))

# get information of a particular method
print(help(str.lower))
