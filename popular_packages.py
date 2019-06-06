import json


def install_sort(package):
	return package['analytics']['30d']


file_path = 'C:\\Users\\Paavan Gopala\\Desktop\\OS-Demo\\New Folder\\packages_info.json'

with open(file_path, 'r') as f:
	data = json.load(f)
	
data = [item for item in data if 'video' in item['desc']]
data.sort(key=install_sort, reverse=True)

data_str = json.dumps(data, indent=2)
print(data_str)
