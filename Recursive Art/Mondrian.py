#  File: Mondrian.py

#  Description: creates random recursive art through the use of turtle in python

#  Student's Name: Evan Johnston

#  Student's UT EID: eaj628

#  Course Name: CS 313E 

#  Unique Number: 53580

#  Date Created: 3/3/14

#  Date Last Modified: 3/7/14

import turtle
import random

class Point (object):
    # creates point class
  def __init__ (self, x = 0, y= 0):
      self.x=x
      self.y=y

class Quad (object):
    # creates quadrilateral object, all quads are rectangles in this case 
    def __init__(self, p1, p2):
        self.p1=Point(p1.x, p1.y)
        self.p2=Point(p2.x, p1.y)
        self.p3=Point(p2.x, p2.y)
        self.p4=Point(p1.x, p2.y)

def draw_line(ttl, x1, y1, x2, y2):
    # draws a straight line, all lines are horizontal or vertical in this case
    ttl.penup()
    ttl.goto (x1, y1)
    ttl.pendown()
    ttl.goto (x2, y2)
    ttl.penup()

def draw_quad(ttl, quad):
    # draws a rectangle
    draw_line(ttl, quad.p1.x, quad.p1.y, quad.p2.x, quad.p2.y)
    draw_line(ttl, quad.p1.x, quad.p1.y, quad.p2.x, quad.p2.y)
    # for some reason after the first iteration of the while loop the first line
    #of a quad does not appear. I doubled it so it would show up
    draw_line(ttl, quad.p2.x, quad.p2.y, quad.p3.x, quad.p3.y)
    draw_line(ttl, quad.p3.x, quad.p3.y, quad.p4.x, quad.p4.y)
    draw_line(ttl, quad.p4.x, quad.p4.y, quad.p1.x, quad.p1.y)

def fill_quad(ttl, quad, color):
    # fills rectangle with color
    ttl.fillcolor(color)
    ttl.begin_fill()
    draw_quad(ttl, quad)
    ttl.end_fill()

def rand_function(p1, p2, n):
    # multi-purpose randomizing function combined for convenience
    
    x=random.randint(p1.x,p2.x)
    y=random.randint(p1.y,p2.y)
    # x and y, which come from input p1 and p2, are used to create a new point
    # that is between the x and y coordinates of the original 2 points

    smallChance=(n*9.5)/100
    bigChance=(1-smallChance)/2
    spin=round(random.uniform(0.0,1.0),3)
    # n is the order of recursion in terms of this function- it scales with order such that
    ## n=1: small Chance= 0.08 and n=6: small chance=0.48
    # the small chance is used for the chance of 'no line' and chance of color
    # big chance is the remaining probabiliy split in 2 (horizontal/vertical and
    # left/right or top/bottom)
    # the spin is the actual random calculation
    # all the information is returned in a list

    return [x,y,smallChance,bigChance,spin]

def draw_mondrian(ttl, num, p1, p2):

    colorList=['red','light blue','yellow','light green','pink','purple','orange','navy']
    shadeList=['white','light grey','dark grey']
    # list of colors and shades to be picked from at random
    
    rando=(rand_function(p1,p2,num))

    p3=Point(rando[0],rando[1])
    xDist=abs(p1.x)+abs(p2.x)
    yDist=abs(p1.y)+abs(p2.y)

    count=0
    while not(p3.x in range (p1.x+10,p2.x-10))or\
          not(p3.y in range (p1.y+10,p2.y-10)):
        rando=rand_function(p1,p2,num)
        p3=Point(rando[0],rando[1])
        count+=1
        if count==10:
            break
        # this keeps the new line being drawn within 10 unit of measure of
        # the previous line. There is a limit at 10 iterations as with higher levels
        # of recursion it becomes too time consuming or impossible to satisfy
    
    zeroChance=rando[2]
    directionChance=rando[3]
    direction=rando[4]           
    
    thickness=random.randint(1,5)
    ttl.pensize(thickness)
    # generates a random thickness of line

    if num>0:
    
        if zeroChance<=direction<directionChance+zeroChance:
            # horizontal
            
            draw_line(ttl, p1.x, p3.y, p2.x, p3.y)
            # draws line

            topP1=Point (p1.x, p3.y)
            topP2=Point (p2.x, p2.y)
            bottomP1=Point (p1.x, p1.y)
            bottomP2=Point (p2.x, p3.y)
            # creates 2 new frames to repeat the process in

            rando1=rand_function(p1,p2,num)
            chanceColor=rando1[2]
            chanceShade=rando1[3]
            fill=rando1[4]
            # randomization for color chance

            topQ=Quad(topP1, topP2)
            bottomQ=Quad(bottomP1, bottomP2)
            # creates the 2 rectangle objects
            shadeChoice=random.randint(0,len(shadeList)-1)
            # choice for shade

            if chanceColor<=fill<chanceColor+chanceShade:
                fill_quad(ttl, topQ, shadeList[shadeChoice])

            elif chanceColor+chanceShade<=fill<=1:
                fill_quad(ttl, bottomQ, shadeList[shadeChoice])

            else:
                choice=random.randint(0,1)
                # choice for top or bottom
                
                colorChoice=random.randint(0,len(colorList)-1)
                # choice for color
                if choice==0:
                    fill_quad(ttl, topQ, colorList[colorChoice])
                else:
                    fill_quad(ttl, bottomQ, colorList[colorChoice])
            
            draw_mondrian (ttl, num-1, topP1, topP2)
            draw_mondrian (ttl, num-1, bottomP1, bottomP2)
            # recursive call until num is 0
            
        elif directionChance+zeroChance<=direction<=1:
            # vertical
            draw_line(ttl, p3.x, p1.y, p3.x, p2.y)

            leftP1=Point (p1.x, p1.y)
            leftP2=Point (p3.x, p2.y)
            rightP1=Point (p3.x, p1.y)
            rightP2=Point (p2.x, p2.y)

            rando1=rand_function(p1,p2,num)
            chanceColor=rando1[2]
            chanceShade=rando1[3]
            fill=rando1[4]

            leftQ=Quad(leftP1, leftP2)
            rightQ=Quad(rightP1, rightP2)
            shadeChoice=random.randint(0,len(shadeList)-1)

            if chanceColor<=fill<chanceColor+chanceShade:
                fill_quad(ttl, leftQ, shadeList[shadeChoice])

            elif chanceColor+chanceShade<=fill<=1:
                fill_quad(ttl, rightQ, shadeList[shadeChoice])

            else:
                choice=random.randint(0,1)
                colorChoice=random.randint(0,len(colorList)-1)
                if choice==0:
                    fill_quad(ttl, leftQ, colorList[colorChoice])
                else:
                    fill_quad(ttl, rightQ, colorList[colorChoice])

            draw_mondrian (ttl, num-1, leftP1, leftP2)
            draw_mondrian (ttl, num-1, rightP1, rightP2)

        else:
            # draw no line            

            quad=Quad(p1, p2)
            
            rando1=rand_function(p1,p2,num)
            chanceColor=rando1[2]
            chanceShade=rando1[3]
            fill=rando1[4]

            shadeChoice=random.randint(0,len(shadeList)-1)
            colorChoice=random.randint(0,len(colorList)-1)

            if chanceColor<=fill<=1:
              fill_quad(ttl, quad, shadeList[shadeChoice])
            else:
              fill_quad(ttl, quad, colorList[colorChoice])

            draw_mondrian (ttl, num-1, p1, p2)    

def main():

    print ('Mondrian Composition')
    print ('')
    print ('This program creates a randomly recursively generated work of art in the\
 abstract style of Piet Mondrian. After each work is created you will have the option\
 to save the image, continue without saving, or exit.')
    print ('')
    begin=str(input('Press any key to begin: '))
    if begin:

      #order= int(input('Enter a level of recursion between 1 and 6: '))
      #while not(0<=order<=6):
          #order= int(input('Enter a level of recursion between 1 and 6: '))

      ttl=turtle.Turtle()
      turtle.title('Recursive Art')
      turtle.setup (800,800,0,0)
      # initialize and set up turtle
      ttl.speed (0)
      ttl.ht()
        
      #if order==0:
      #     turtle.done()
      #     return
        
      count=1
      import time
      
      while True:
        frame1=Point (-370, -350)
        frame2=Point (370, 325)
        frame=Quad(frame1, frame2)
        ttl.color ('black')
        ttl.pensize(10)
        draw_quad(ttl, frame)
        # draws frame in which Mondrian-esque work created
        order=random.randint(1,8)

        ttl.ht()
        ttl.penup()
        ttl.goto(0,350)
        ttl.write('Piece '+str(count)+'- Recursive order: '+str(order), False, align='center', font=('Arial', 18, 'bold'))

        draw_mondrian(ttl, order, frame1, frame2)
        count+=1
        
        answer=str(input('To save press Y, to continue press N, to exit press E: '))

        t=time.localtime()
        sec=str(t[5])
        minet=str(t[4])
        hour=str(t[3])
        day=str(t[2])
        mon=str(t[1])
        year=str(t[0])

        now=day+'/'+mon+'/'+year+' - '+hour+':'+minet+':'+sec
        if answer=='y' or answer=='Y':
            ts = ttl.getscreen().getcanvas()
            ts.postscript(file='Mondrian'+str(count)+'.eps')
            turtle.clearscreen()
            
        elif answer=='e' or answer=='E':       
            turtle.clearscreen()
            break
          
        else:
            turtle.clearscreen()
            continue
         
    ttl.penup()
    ttl.goto(0,0)
    ttl.write('Byeeeee <3', False, align='center', font=('Arial', 36, 'bold'))
    time.sleep(2)
    print ('Byeeeee <3')
    turtle.bye()
    return
   
main()

