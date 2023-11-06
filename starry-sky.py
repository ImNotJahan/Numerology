'''
Creates a drawing of a starry sky from a name
'''

from turtle import *
from random import randint, seed
from PIL import Image
from common import parse_number

strname = input("Name? ")
# converts name to number
name = parse_number(strname)

# how many times it should draw star patterns
iterations = int(input("Iterations? "))

bgcolor("black")

# because background doesn't show up in .eps file
# https://stackoverflow.com/a/13540724/
def draw_background():
    ts = getscreen()
    canvas = ts.getcanvas()
    height = ts.getcanvas()._canvas.winfo_height()
    width = ts.getcanvas()._canvas.winfo_width()

    turtleheading = heading()
    turtlespeed = speed()
    penposn = position()
    penstate = pen()

    penup()
    speed(0)
    goto(-width/2-2, -height/2+3)
    fillcolor("black")
    begin_fill()
    setheading(0)
    forward(width)
    setheading(90)
    forward(height)
    setheading(180)
    forward(width)
    setheading(270)
    forward(height)
    end_fill()

    penup()
    setposition(*penposn)
    pen(penstate)
    setheading(turtleheading)
    speed(turtlespeed)

draw_background()

penup()
pencolor("white")

hideturtle()

title("\u2605 " + strname + " \u2605")

seed(name)
speed(0)

# draws a star shape
def star():
    for i in range(5):
        pendown()
        forward(5)
        right(144)
        penup()

for i in range(0, iterations):
    '''
    each iter goes to a different pos, but every
    run will produce the same output for the
    same input, as the seed is set to the name
    '''
    goto(randint(-300,300),randint(-300,300))
    
    temp = str(name)

    state = 0
    # draws stars based on name
    while len(temp) > 0:
        digit = int(temp[0])
        temp = temp[1:]

        if(state == 0):
            if(digit % 2 == 0):
                forward(digit * 30)
            else:
                backward(digit * 30)
        elif(state == 1):
            if(digit % 2 == 0):
                left(digit * 36)
            else:
                right(digit * 36)
        else:
            star()

        state = (state + digit) % 3

# everything past here is just for saving the image as
# a png (when you press 's')
def save():
    Screen().getcanvas().postscript(file=strname + ".eps", colormode="color")

    # note that ghostscript must be downloaded (and in path)
    # for this part to work
    img = Image.open(strname + ".eps")
    img.save(strname + ".png", "png")
    
onkeyrelease(save, 's')
listen()

done()
