#  File: Goldbach.py

#  Description: Uses Goldbach's Conjecture to show all possible prime sums for 
#even integers for a given range>=4 where both limits are even. Also returns 
#longest string of pairs.

#  Student Name: Evan Johnston

#  Student UT EID: eaj628

#  Course Name: CS 303E

#  Unique Number: 53590

#  Date Created: 10/21/13

#  Date Last Modified: 10/22/13

def is_prime (n):
  limit = int (n ** 0.5) + 1
  for divisor in range (2, limit):
    if (n % divisor == 0):
      return False
  if n==0 or n==1:
      return False
  return True
#is_prime function from class determines of a number (n) is prime or not

def main():
  lo=int(input('Enter lower limit: '))
  up=int(input('Enter upper limit: '))
  #user defines the upper and lower limits of range
  print ('')

  while lo>up or lo<4 or lo%2!=0 or up%2!=0:
    lo=int(input('Enter lower limit: '))
    up=int(input('Enter upper limit: '))
    #lo and up must be even, >=4, and lo<=up
    print ('')

  maxCount=0
  #initialize total count to find longest strain
  
  for i in range (lo,up+1,2):
      #this loop iterates for the user defined range
      
      print (i,end=' ')
      #starts each line with even number, beginning with the input number
      
      pcount=0
      #initialize count of prime number pairs
      
      for n in range (2,i//2+1):
        #this loop iterates for all numbers to find the primes in the defined range
        #2, the first prime, and i//2 to prevent doubles from occuring (2+3 and 3+2)
        
        if is_prime(n):
          d=i-n
          #difference is the total-number in trial
          
          if is_prime(d):
            pcount+=1
            #if both are prime, n and d, the count of prime number pairs is incremented
            
            if pcount>maxCount:
              maxCount=pcount
              #moves the maximum count to the largest increment of prime pairs
              
            print ('=',n,'+',d,end=' ')
            #prints the statements on the same line for each even number i
            
      print ()
      #resets to a new line after loop ends
      
  print ('')
  print ('The maximum number of pairs =',maxCount)
  #prints the maximum number of pairs
   
main()
