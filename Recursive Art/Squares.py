# File: Squares.py

# Description: Draws squares of different sizes

import turtle
import random

# draw a square of a given side 
# starting at uuper left corner (x, y)
def drawSquare (ttl, x, y, side):
  ttl.penup()
  ttl.goto(x, y)
  ttl.setheading(0)	# set the pen in the +ve x direction
  ttl.pendown()
  for iter in range (4):
    ttl.forward(side)
    ttl.right(90)
  ttl.penup()

def drawFilledSquare (ttl,x,y,side,color):
  ttl.fillcolor(color)
  ttl.begin_fill()
  drawSquare (ttl,x,y,side)
  ttl.end_fill()
 
def random_color():
    COLOR_RANGE = (50, 255)
    
    rgb = list()
    for c in range(0, 3):
        rgb.append(random.randrange(COLOR_RANGE[0], COLOR_RANGE[1]))
    
    return '#'+"".join([hex(c)[2:].upper() for c in rgb])

def main():

  # put label on top of page
  turtle.title ('Squares')

  # setup screen size
  turtle.setup (1200, 1200, 0, 0)

  # create a turtle object
  ttl = turtle.Turtle()

  # assign a color to the turtle object
  ttl.color ('red')

  # draw multiple squares
##  drawSquare (ttl, -50, -50, 50)
##  drawSquare (ttl, 0, 0, 50)
##  drawSquare (ttl, 50, 50, 50)
##  drawSquare (ttl, -50, 50, 150)

  # fill a closed region
##  ttl.fillcolor ('purple')
##  ttl.begin_fill()
##  drawSquare (ttl, 0, 0, 50)
##  ttl.end_fill()

  # draw chess board
  ttl.speed(0)

  for i in range (1,8,2):
    for k in range (1,8,2):
      drawFilledSquare (ttl,k*50,i*50,50,'black')
    for l in range (2,9,2):
      drawFilledSquare (ttl,l*50,i*50,50,'white')
  for j in range (2,9,2):
    for m in range (1,8,2):
      drawFilledSquare (ttl,m*50,j*50,50,'white')
    for n in range (2,9,2):
      drawFilledSquare (ttl,n*50,j*50,50,'black')

  # persist drawing
  turtle.done()

main()

