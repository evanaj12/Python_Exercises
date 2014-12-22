#  File: Hailstone.py

#  Description: Collatz Conjecture tester: for a given range reports the integer 
# with the longest valid collatz reduction to one

#  Student Name:Evan Johnston

#  Student UT EID:eaj628

#  Course Name: CS 303E

#  Unique Number:53590 

#  Date Created:10/10/13

#  Date Last Modified:10/11/13

def main():

 start=int(input("Enter starting number of the range: "))
 #prompt user to enter starting value for range

 end=int(input("Enter ending number of the range: "))
 #prompt user to enter ending value for range
 
 while start>end or start<=0:
     start=int(input("Enter starting number of the range: "))
     end=int(input("Enter ending number of the range: "))
     #this loop corrects for user input error
 if start==1 and end==1:
     print ('The number 1 has the longest cycle length of 0.')
     #this conditional is for the special case of 1 to 1
     
 j=0
 #j is the integer that will lead the iterations in the loop
 k=0
 #k is the changing version of j, so that j is preserved
 max=0
 #max is the maximum number of cycles
 max_num=0
 #max_num is the number associated with max
 
 for j in range (start,end+1):
    count=0
    k=j
    while k!=1:
        if k%2==0:
            k=k//2
        else:
            k=k*3+1
        count=count+1
    if count>max:
        max=count
        max_num=j
 #this loop performs the Collatz Conjecture on the read range while
 #incrementing the count of number of iterations completed
 #it then stores the max values in the final conditional

 print ('The number',max_num,'has the longest cycle length of '+str(max)+'.')
 #returns the results

main ()
