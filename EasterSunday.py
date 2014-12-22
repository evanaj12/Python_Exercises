#  File: EasterSunday.py

#  Description: Calculation of date of Easter Sundays

#  Student Name: Evan Johnston

#  Student UT EID: eaj628

#  Course Name: CS 303E

#  Unique Number: 53590

#  Date Created: 9/24/13

#  Date Last Modified:9/24/13

def main():
  y=int(input("Enter year: "))

  #Prompt user to enter year
  
  a= y%19
  
  b= y//100
  
  c= y%100
  
  d= b//4
  
  e= b%4
  
  g= (8*b+13)//25
  
  h= (19*a+b-d-g+15)%30
  
  j= c//4
  
  k= c%4
  
  m= (a+11*h)//319
  
  r= (2*e+2*j-k-h+m+32)%7
  
  n= (h-m+r+90)//25
  
  p= (h-m+r+n+19)%32

  #Gauss's algorithm	

  if n==3: 
    month="March"
  if n==4:
    month="April"

  #Conditionals to determine month based on 'n'
    
  print ("In"+" "+str(y)+" Easter Sunday is on"+" "+str(p)+" "+(month))

  #Print output of date of Easter Sunday
  
main()
