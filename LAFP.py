class Duck:
	
	def quack(self):
		print('Quack, quack')
	
	def fly(self):
		print('Flap, flap!')


class Person:
	
	def quack(self):
		print("I'm quacking like a duck")
	
	def fly(self):
		print("I'm flapping my arms")


def quack_and_fly(thing):
	# EAFP (Pythonic)

	try:
		thing.quack()
		thing.fly()
		# thing.bark()
	except AttributeError as a:
		print(a)

	print()


d = Duck()
quack_and_fly(d)

p = Person()
quack_and_fly(p)
