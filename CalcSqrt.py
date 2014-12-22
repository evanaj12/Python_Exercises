#  File: CalcSqrt.py

#  Description:Method for calculating square root

#  Student Name:Evan Johnston

#  Student UT EID:eaj628

#  Course Name: CS 303E

#  Unique Number: 53590

#  Date Created:10/6/13

#  Date Last Modified:10/7/13

def main():
    n=float(input("Enter a positive number: "))

    #prompt user to input a positive number

    while n<0:
        n=float(input("ERROR. PLEASE ENTER VALID POSITIVE NUMBER: "))

    #continue to prompt user for a positive number if input invalid

    oldGuess=n/2.0
    newGuess=((n/oldGuess)+oldGuess)/2.0

    #apply Newton's Method for calculation of square root

    while abs(newGuess-oldGuess)>(.000001):
        oldGuess=newGuess
        newGuess=((n/oldGuess)+oldGuess)/2.0

    #while loop to apply the algorithm until within 0.000001 discrepancy.
 
    actual=n**0.5
    d=newGuess-actual

    #find difference with actual square

    print ("Square root is:",(newGuess))
    print ("Difference is: ",(d))

    #output results
    
main()
