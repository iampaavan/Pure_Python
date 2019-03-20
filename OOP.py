class Person(object):
	
	def __init__(self, name):
		self.name = name
		
	def reveal_identity(self):
		print(f'My name is: {self.name}')
		

class SuperHero(Person):
	
	def __init__(self, name, hero_name):
		super(SuperHero, self).__init__(name)
		self.hero_name = hero_name
		
	def reveal_identity(self):
		super(SuperHero, self).reveal_identity()
		print(f'...And i am {self.hero_name}')
		

# paavan = Person('Paavan')
# paavan.reveal_identity()

# print(issubclass(SuperHero, Person))
wade = SuperHero('Wade', 'Deadpool')
wade.reveal_identity()
print(isinstance(wade, SuperHero))
