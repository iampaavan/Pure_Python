my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#          0, 1, 2, 3, 4, 5, 6, 7, 8, 9
#        -10,-9,-8,-7,-6,-5,-4,-3,-2,-1

# list[start:end:step]

print(my_list[0:6])
print(my_list[4:9])
print(my_list[1:])
print(my_list[:6])
print(my_list[2:-1:2])
print(my_list[-1:2:-1])
print(my_list[-2:1:-2])
print(my_list[::-1])

my_url = 'http://www.gmail.com'

# reverse the URL
print(my_url[::-1])

# get the TLD
print(my_url[-4:])

print(my_url.index('w'))
# print the url without http://
print(my_url[7:])

print(my_url.index('l'))
# print the url without http:// and TLD
print(my_url[7:16])
