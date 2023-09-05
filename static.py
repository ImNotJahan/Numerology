'''
Generates an image of random static containing a name
'''

from PIL import Image, ImageColor
from common import parse_number, rand_bool

width = int(input("Width? "))
height = int(input("Height? "))

# a new image is by default all black,
# so we only need to add white
white = ImageColor.getcolor('white', '1')

str_name = input("Name? ")
# converts to binary
name = bin(parse_number(str_name))[2:]

# one = white = true
def parse_digit(string, index):
    return string[index] == '1'

name_length = len(name)

found_name = False

while not found_name:
    # the '1' means that it's only black and white
    img = Image.new('1', (width, height))
    name_index = 0
    
    for y in range(0, height):
        for x in range(0, width):
            value = rand_bool()

            # true = white
            if(value):
                img.putpixel((x, y), white)
            # otherwise it's default black
            
            if not found_name:
                if value == parse_digit(name, name_index):
                    name_index += 1

                    if(name_index == name_length):
                        found_name = True
                        print("\nFound (end) at " + str((x, y)))
                        print("Name should look like " + name)

                else:
                    name_index = 0

img.save(str_name + ".png")
print("Saved to " + str_name + ".png")
