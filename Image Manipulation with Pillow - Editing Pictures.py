from PIL import Image, ImageFilter
import os

# image1 = Image.open('C:\\Users\\Paavan Gopala\\Desktop\\OS-Demo\\New Folder\\Images\\700\\pup_1_700.jpg')
# image1.show()

# image1.rotate(90).save('C:\\Users\\Paavan Gopala\\Desktop\\OS-Demo\\New Folder\\Images\\700\\pup_1_700_modified.jpg')
image1 = Image.open('C:\\Users\\Paavan Gopala\\Desktop\\OS-Demo\\New Folder\\Images\\700\\pup_1_700.jpg')
image1.convert(mode='L').save('C:\\Users\\Paavan Gopala\\Desktop\\OS-Demo\\New Folder\\Images\\700\\pup_1_700_black.jpg')
image1 = Image.open('C:\\Users\\Paavan Gopala\\Desktop\\OS-Demo\\New Folder\\Images\\700\\pup_1_700_black.jpg')
# image1.show()

image2 = Image.open('C:\\Users\\Paavan Gopala\\Desktop\\OS-Demo\\New Folder\\Images\\700\\pup_2_700.jpg')
image2.filter(ImageFilter.GaussianBlur(15)).save('C:\\Users\\Paavan Gopala\\Desktop\\OS-Demo\\New Folder\\Images\\700\\pup_2_700_blur.jpg')
image2 = Image.open('C:\\Users\\Paavan Gopala\\Desktop\\OS-Demo\\New Folder\\Images\\700\\pup_2_700_blur.jpg')
image2.show()

