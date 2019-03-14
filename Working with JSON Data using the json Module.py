import json

people_string = '''
{
  "people": [
  {
    "name": "Paavan Gopala",
    "phone": "615-000-4651",
    "emails": ["paavangopala@bogusemail.com", "paavan.gopala@work-place.com"],
    "has-license": false
  },
  {
    "name": "Thilak Raj",
    "phone": "808-999-4651",
    "emails": null,
    "has-license": true
  }
 ]
}
'''

data = json.loads(people_string)

print()
print(data)
print()
print(type(data))
print(type(data['people']))
print()

for person in data['people']:
	
	print(person)
	# print(person['name'])
	print()
	del person['phone']
	
print()
new_string = json.dumps(data, indent=2)
# new_string = json.dumps(data, indent=2, sort_keys=True)
print(new_string)


