#  File: Day.py

#  Description:Your program will print out the day of the week for the entered date.

#  Student Name: Evan Johnston

#  Student UT EID:eaj628

#  Course Name: CS 303E

#  Unique Number: 53590

#  Date Created:9/30/13

#  Date Last Modified:9/30/13

def main():
  y0=int(input("Enter year: "))
  m0=int(input("Enter month: "))
  d0=int(input("Enter day: "))
  #Prompt user to put in year, month, and day.

  if 3<=m0<=12:
      a=(m0-2)
  elif m0==1:
      a=11
  elif m0==2:
      a=12
  #Convert input month (m0) to Zeller month (a)

  b=d0
  #Set input day (d0) to Zeller day (b)

  if (m0==1) or (m0==2):
    c=(y0-1)%100
  else:
    c=y0%100
  '''Set (c) to year of the century, the last 2 digits;
  account for Zeller Jan and Feb'''

  if (m0==1) or (m0==2):
    d=(y0-1)//100
  else:
    d=y0//100
  '''Set (d) to century, the first 2 digits;
  account for Zeller Jan and Feb'''

  w=(13*a-1)//5 
  x=c//4 
  y=d//4 
  z=w+x+y+b+c-2*d 
  r=z%7 
  r=(r+7)%7
  #Use Zeller algorithm.

  if r==0:
    day="Sunday"
  elif r==1:
    day="Monday"
  elif r==2:
    day="Tuesday"
  elif r==3:
    day="Wednesday"
  elif r==4:
    day="Thursday"
  elif r==5:
    day="Friday"
  elif r==6:
    day="Saturday"
  #Set (r) to respective weekday

  print ("The day is "+(day))
  #Output the correct weekday based on year, month, and day.
main()
