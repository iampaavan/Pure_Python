import requests
import json
import time

url = 'https://formulae.brew.sh/api/formula.json'

response = requests.get(url)
packages_json = response.json()
results = []

t1 = time.perf_counter()

for package in packages_json:
	package_name = package['name']
	package_desc = package['desc']
	package_url = f'https://formulae.brew.sh/api/formula/{package_name}.json'
	
	try:
		response = requests.get(package_url)
		package_json = response.json()
		# print(package_json)
		package_string = json.dumps(package_json, indent=2)
		
		install_30 = package_json['analytics']['install_on_request']['30d'][package_name]
		install_90 = package_json['analytics']['install_on_request']['90d'][package_name]
		install_365 = package_json['analytics']['install_on_request']['365d'][package_name]
	
	except Exception:
		continue
	
	data = {
		'name': package_name,
		'desc': package_desc,
		'analytics': {
			'30d': install_30,
			'90d': install_90,
			'365d': install_365
		}
	}
	
	results.append(data)
	# time.sleep(response.elapsed.total_seconds())
	print(f"Got {package_name} in {response.elapsed.total_seconds()} seconds.")
	
t2 = time.perf_counter()
print(f"Total Time: {t2 - t1} seconds.")

file_path = 'C:\\Users\\Paavan Gopala\\Desktop\\OS-Demo\\New Folder\\packages_info.json'

with open(file_path, 'w') as file_writer:
	json.dump(results, file_writer, indent=2)

