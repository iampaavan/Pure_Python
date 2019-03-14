import json

with open('US_States.json', 'r') as f:
	data = json.load(f)
	print(data)

for state in data['states']:
	#print(state)
	print()
	print(state['name'], state['abbreviation'])

for delete in data['states']:
	del delete['area_codes']

print()
# print(data['states'])

with open('new_us_states', 'w') as w:
	json.dump(data, w, indent=2)
