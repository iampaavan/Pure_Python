import os, glob

os.chdir('C:\\Users\\Paavan Gopala\\Desktop\\OS-Demo\\New Folder')

for photos in glob.glob("*.jpg"):
	print(photos)
