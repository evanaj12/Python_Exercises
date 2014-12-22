#  File: CalculatePI.py

#  Description: calculaton of pi using random numbers

#  Student Name: Evan Johnston

#  Student UT EID: eaj628

#  Course Name: CS 303E

#  Unique Number: 53590

#  Date Created: 10/17/13

#  Date Last Modified: 10/18/13

import math
import random

def computePI (numThrows):
    #this fuction will compute an approximate value of pi using random numbers

    circleDarts=0

    for i in range(0,numThrows+1):

      xPos = random.uniform (-1.0, 1.0)
      #generates random (x) coordinate of a 'thrown dart'
      
      yPos = random.uniform (-1.0, 1.0)
      #generates random (y) coordinate of a 'thrown dart'
      
      d=math.hypot(xPos,yPos)
      #calculates distance from the (x,y) dart point to the origin

      if d<1:
          circleDarts=circleDarts+1
          #if the dart falls within the radius, r=1, of the circle cricleDarts is incremented
          
      piCalc=circleDarts/numThrows*4
      #calculates appoximate value of pi based on the ratio circleDarts/numThrows=pi/4

    return piCalc

def main ():
    print ('Computation of PI using Random Numbers')
    print ('')

    numThrows=100
    #initialize numThrows, the number of times the 'dart' is thrown

    while numThrows!=100000000:
      #this loop repeats the calculation for 100 to 10000000 by powers of 10

      piCalc=computePI(numThrows)
      #calls computePI function
      piCalc=round(piCalc,6)

      dif=round(piCalc-math.pi,6)
      #calculates difference between calulated pi and the accepted value of pi

      if numThrows==100:
            print ('num =%-d '%numThrows,'      Calculated PI = %0f'%piCalc,'   Difference = %+f'%dif)
      elif numThrows==1000:
            print ('num =%-d '%numThrows,'     Calculated PI = %0f'%piCalc,'   Difference = %+f'%dif)
      elif numThrows==10000:
            print ('num =%-d '%numThrows,'    Calculated PI = %0f'%piCalc,'   Difference = %+f'%dif)
      elif numThrows==100000:
            print ('num =%-d '%numThrows,'   Calculated PI = %0f'%piCalc,'   Difference = %+f'%dif)
      elif numThrows==1000000:
            print ('num =%-d '%numThrows,'  Calculated PI = %0f'%piCalc,'   Difference = %+f'%dif)
      elif numThrows==10000000:
            print ('num =%-d '%numThrows,' Calculated PI = %0f'%piCalc,'   Difference = %+f'%dif)
      #prints numThrows, piCalc, and dif with required formatting

      numThrows=numThrows*10
      #increments numThrows with powers of 10     
    
    print ('')
    print ('Difference = Calculated PI - math.pi')

main()
