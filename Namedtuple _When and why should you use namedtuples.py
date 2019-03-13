from collections import namedtuple

# colors_tuple = 55, 155, 255)
# colors_dict = {'red': 55, 'green': 155, 'blue': 255}
# print(colors_dict['red'])

Color = namedtuple('Color', ['red', 'green', 'blue'])
color = Color(55, 155, 255)
white = Color(255, 255, 255)
# print(color[0], color[1], color[2])
# print(color)
# print(color[0])
print(color.red)
print(white.red)

