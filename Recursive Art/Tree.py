
import turtle
import random

# draw a tree recursively
def drawTree3 (ttl, length):
  if length > 5:
    ttl.pensize (length//8)
    ttl.forward (length)
    ttl.right (40)
    ttl.color ('brown')
    drawTree3 (ttl, length-20)
    ttl.left (40)
    drawTree3 (ttl, length-20)
    ttl.left (40)
    drawTree3 (ttl, length-20)
    ttl.right (40)
    color=random_select_color()
    ttl.color (color,color)
    ttl.begin_fill()
    ttl.circle(6)
    ttl.end_fill()
    ttl.color ('brown')
    ttl.backward (length)

def drawTree2 (ttl, length):
  if length >4:
    ttl.pensize(length//8)
    ttl.forward (length)
    ttl.right (30)
    ttl.color ('brown')
    drawTree2 (ttl, length-15)
    ttl.left (60)
    drawTree2 (ttl, length-15)
    ttl.right (30)
    color=random_select_color()
    ttl.color (color,color)
    ttl.begin_fill()
    ttl.circle(6)
    ttl.end_fill()
    ttl.color ('brown')
    ttl.backward (length)

def random_select_color():
  n=random.randint(1,5)
  if n==1:
    return 'red'
  elif n==2:
    return 'orange'
  elif n==3:
    return 'yellow'
  elif n==4:
    return 'brown'
  elif n==5:
    return 'green'
  

def main():
  # prompt the user to enter a branch length
  length = 100
  #int (input ('Enter branch length: '))

  # put label on top of page
  turtle.title ('Recursive Tree')

  # setup screen size
  turtle.setup (800, 800, 0, 0)

  # create Turtle object
  ttl = turtle.Turtle()

  # assign a color to the turtle object
  #ttl.color ('brown')
  ttl.speed(0)

  # draw the tree
  ttl.penup()
  ttl.goto (-100, -300)
  ttl.pendown()
  ttl.left (90)
  ttl.pendown()
  drawTree2 (ttl, length)
  
  ttl.penup()
  ttl.goto (100, 0)
  ttl.pendown()
  ttl.pendown()
  ttl.color ('brown')
  drawTree3 (ttl, length)
  ttl.penup()

  # persist drawing
  turtle.done()

main()
