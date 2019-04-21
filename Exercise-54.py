import os
"""Write a python program to access environment variables."""
print(f'***************************************************')
print(os.environ)
print(f'***************************************************')

try:
	os.mkdir('C:\\Users\\Paavan Gopala\\Desktop\\OS-Demo-2')
	os.makedirs('C:\\Users\\Paavan Gopala\\Desktop\\OS-Demo-3\\New-Folder')
	
except Exception:
	print(f'Folder already present.')
	
else:
	print(f'Folders created successfully.')
