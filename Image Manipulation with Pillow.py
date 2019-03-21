from PIL import Image
import os

size_300 = (300, 300)
size_700 = (700, 700)

print(os.getcwd())
os.chdir('C:\\Users\\Paavan Gopala\\Desktop\\OS-Demo\\New Folder\\Images')
print(os.getcwd())

# iterate through the folder structure containing the images.
for f in os.listdir('.'):
	if f.endswith('.jpg'):
		# print(f) # print all the images with extension .jpg
		i = Image.open(f) # create an image object
		file_name, file_extension = os.path.splitext(f) # split the image file into filename and file extension
		i.thumbnail(size_700)
		i.save(f'C:\\Users\\Paavan Gopala\\Desktop\\OS-Demo\\New Folder\\Images\\700/{file_name}_700{file_extension}')
		# print(file_name)
		i.thumbnail(size_300) # resizing the image using a tuple
		"""save the images in a separate folder as .png extension"""
		# i.save(f'C:\\Users\\Paavan Gopala\\Desktop\\OS-Demo\\New Folder\\Images\\pngs/{file_name}.png')
		i.save(f'C:\\Users\\Paavan Gopala\\Desktop\\OS-Demo\\New Folder\\Images\\300/{file_name}_300{file_extension}')

# image1 = Image.open('C:\\Users\\Paavan Gopala\\Desktop\\OS-Demo\\New Folder\\Images\\pup_1.jpg')
# image1.show()
# image1.save('C:\\Users\\Paavan Gopala\\Desktop\\OS-Demo\\New Folder\\Images\\pup_1.png')

image1 = Image.open('C:\\Users\\Paavan Gopala\\Desktop\\OS-Demo\\New Folder\\Images\\700\\pup_1_700.jpg')
image1.show()
