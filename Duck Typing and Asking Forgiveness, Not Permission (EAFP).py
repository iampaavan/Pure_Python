# Duck Typing and Easier to ask Forgiveness than Permission (EAFP)


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
	
	# Not duck typed (Non-Pythonic)
	if isinstance(thing, Duck):
		thing.quack()
		thing.fly()
	else:
		print('This has to be a Duck !!')

	print()
	
	
print('*******************************************************************')


def quack_and_fly_1(things):
	
	things.quack()
	things.fly()
	
	print('Inside the second quack and fly method')
	print('*****************************************************************')
	
	
d = Duck()
quack_and_fly(d)

p = Person()
quack_and_fly(p)

d_1 = Duck()
quack_and_fly_1(d_1)

p_1 = Person()
quack_and_fly_1(p_1)

