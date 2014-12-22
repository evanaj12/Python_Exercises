#  File: GuessingGame.py

#  Description: Program will return user chosen number within 7 guesses

#  Student Name: Evan Johnston

#  Student UT EID: eaj628

#  Course Name: CS 303E

#  Unique Number: 53590

#  Date Created: 11/18/13

#  Date Last Modified: 11/20/13

def single_binSearch(a,n):
    #function that completes 1 iteration of a binary search
    
    lo=a[0]
    #the first character of the list being searched
    
    hi=a[-1]
    #the last character of the list being searched
    
    mid=(lo+hi)//2
    #the middle character of the list
    
    b=[]
    #empty list where new list will form
    
    prevMid=mid
    #the current mid value, which will be the previous mid after the function completes

    prevA=a
    
    if n=='-1':
        lo=mid+1
        mid=(lo+hi)//2
        #sets lo to the mid+1 and updates the mid
        
        for i in range (lo,hi+1):
            b.append(i)
            #creates new list in the new range
            
        return (b,mid,prevMid,prevA)
        #returns the new list, the mid (guess), and the previous mid
    
    else:
        hi=mid-1
        mid=(lo+hi)//2
        for i in range (lo,hi+1):
            b.append(i)
        return (b,mid,prevMid,prevA)
        #same as above but for the upper half of the input list
    
def main ():

    print ('Guessing Game')
    print ('')
    print ('Think of a number between 1 and 100 inclusive.')
    print ('And I will guess what it is in 7 tries or less.')
    print ('')
    #formatting and explanation of game
    
    yn=str(input('Are you ready? (y/n): ' ))
    #yes or no input

    while not((yn=='y') or (yn=='n')):
        yn=str(input('Are you ready? (y/n): '))
    print ('')
    #continues to prompt if invalid response given

    if yn=='y':
        a=[]
        for i in range (1,101):
            a.append(i)
            #creates the list of 100 numbers that is the starting point of all consecutive lists
            
        print ('Guess  1 :  The number you thought was 50')
        n=str(input('Enter 1 if my guess was high, -1 if low, and 0 if correct: '))
        #initial guess is always 50 and first guess, n, determines directionality of the search
        
        count=1
        flag=True
        while n!='0':
            #for all cases where guess is incorrect, or user input incorrect
 
            if count>7:
                print ('')
                print ('Either you guessed a number out of range or you had an incorrect entry.')
                return
                #count used to keep guesses <=7, ends program if at 7 guesses

            if flag:
                (a,mid,prevMid,prevA)=single_binSearch(a,n)
                count+=1
                #calls function with each new list as it narrows down
 
            else:
                (a,mid,prevMid,prevA)=single_binSearch(prevA,n)
                flag=True
                #if the user has put in an invalid input, uses the previous list and resets the flag

            if n=='1':
                print ('')
                print('Guess ',count,' :  The number you thought was',mid)
                #prints guess number and guess for lower half
                       
            if n=='-1':
                print ('')
                print('Guess ',count,' :  The number you thought was',mid)
                #prints guess number and guess for upper half

            while not((n=='1') or (n=='-1') or (n=='0')):
                flag=False
                print ('')
                print('Guess ',count-1,' :  The number you thought was',prevMid)
                n=str(input('Enter 1 if my guess was high, -1 if low, and 0 if correct: '))
                #if user input is wrong, for the guess, iterates until correct

            if flag:
                n=str(input('Enter 1 if my guess was high, -1 if low, and 0 if correct: '))
                #if the user has put in an invalid input, skips this input to avoid redundancy
              
        if n=='0':
            print ('')
            print ('Thank you for playing the Guessing Game.')
            return
            #ends program once correct guess presented
        
    if yn=='n':
        print ('Bye')
        return
        #ends program if user input 'n', no
           
main()
