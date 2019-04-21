"""Write a Python program to test whether a passed letter is a vowel or not."""


def check_vowels(char):
	""":return boolean if the char is a vowel or not."""
	all_vowels = 'aeiou'
	return char in all_vowels


print(f"Check if 'c' is a vowel: {check_vowels('c')}")
print(f'***************************************************')
print(f"Check if 'u' is a vowel: {check_vowels('u')}")
print(f'***************************************************')
