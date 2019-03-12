import random

print()
value_0_1 = random.random()
print('Random value between 0 and 1: ', value_0_1)

print('****************************************************')

print()
value_float = random.uniform(1, 10)
print('Random float value between 1 and 10: ', value_float)

print('****************************************************')

print()
value_int = random.randint(1, 7)
print('Random int value between 1 and 7: ', value_int)

print('****************************************************')

print()
greetings = ['Hi', 'Hello', 'Hola', 'Howdy', 'Hey']
random_list = random.choice(greetings)
print(random_list, ', Paavan')

print('****************************************************')

print()
colors = ['Red', 'Black', 'Green']
random_colors = random.choices(colors)
print(random_colors)
random_colors_1 = random.choices(colors, k=10)
print(random_colors_1)
random_colors_2 = random.choices(colors, weights=[18, 18, 2], k=10)
print(random_colors_2)

print('****************************************************')

print()
deck = list(range(1, 53))
random.shuffle(deck)
print(deck)

print('****************************************************')

print()
deck_1 = list(range(1, 53))
hand = random.sample(deck_1, k=5)
print(hand)

print('****************************************************')
print()


first_names = ['John', 'Jane', 'Corey', 'Travis', 'Dave', 'Kurt', 'Neil', 'Sam', 'Steve', 'Tom', 'James', 'Robert', 'Michael', 'Charles', 'Joe', 'Mary', 'Maggie', 'Nicole', 'Patricia', 'Linda', 'Barbara', 'Elizabeth', 'Laura', 'Jennifer', 'Maria']

last_names = ['Smith', 'Doe', 'Jenkins', 'Robinson', 'Davis', 'Stuart', 'Jefferson', 'Jacobs', 'Wright', 'Patterson', 'Wilks', 'Arnold', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor', 'Anderson', 'Thomas', 'Jackson', 'White', 'Harris', 'Martin']

street_names = ['Main', 'High', 'Pearl', 'Maple', 'Park', 'Oak', 'Pine', 'Cedar', 'Elm', 'Washington', 'Lake', 'Hill']

fake_cities = ['Metropolis', 'Eerie', "King's Landing", 'Sunnydale', 'Bedrock', 'South Park', 'Atlantis', 'Mordor', 'Olympus', 'Dawnstar', 'Balmora', 'Gotham', 'Springfield', 'Quahog', 'Smalltown', 'Epicburg', 'Pythonville', 'Faketown', 'Westworld', 'Thundera', 'Vice City', 'Blackwater', 'Oldtown', 'Valyria', 'Winterfell', 'Braavos‎', 'Lakeview']

states = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']

with open('C:\\Users\\Paavan Gopala\\Desktop\\OS-Demo\\New Folder\\address.txt', 'w', encoding="utf-8") as file_handler:
	
	for num in range(100):
		first = random.choice(first_names)
		last = random.choice(last_names)
		phone = f'{random.randint(100, 999)}-555-{random.randint(1000,9999)}'
		street_num = random.randint(100, 999)
		street = random.choice(street_names)
		city = random.choice(fake_cities)
		state = random.choice(states)
		zip_code = random.randint(10000, 99999)
		address = f'{street_num} {street} St., {city} {state} {zip_code}'
		email = first.lower() + last.lower() + '@bogusemail.com'
		blank = "\n"
		file_handler.write(f'{first} {last}\n{phone}\n{address}\n{email}\n{blank}')



