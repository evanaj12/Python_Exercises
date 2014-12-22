#  File: Nim.py

#  Description: For each Nim game, given a number of heaps each with a number of counts, 
#  the program tells if the first player would lose the Nim game or how much should
#  be taken from each heap in order to win.

#  Student's Name: Evan Johnston

#  Student's UT EID: eaj628
 
#  Course Name: CS 313E 

#  Unique Number: 53580

#  Date Created: 1/15/14

#  Date Last Modified: 1/17/14

def main ():
    infile=open('nim.txt','r')
    text=infile.read()
    text=text.split('\n')
    # reads in nim file with information and removes newline character
    
    games=int(text[0])
    gamesList=text[1:]
    # isolates the first line that indicates the number of games and creates a list
    # where the game heaps are stored
    
    for heaps in range (0,games):
        heapList=gamesList[heaps]
        heapList=heapList.split(' ')
        # loop iterates for the number of games and creates a list of the heaps
        # each game
        
        intHeapList=[]
        # new list for the integer conversion of the contents of the list
        
        leng=len(heapList)

        for i in range (0,leng):
            intHeapList.append(int(heapList[i]))
        # converts all string digits to integers and puts them in new list

        nimSum=intHeapList[0]
        # initializes nimSum with the first integer
        
        for i in range (1,leng):
            nimSum=nimSum^intHeapList[i]
        # sums all the values to the nimSum as needed
            
        if nimSum==0:
            print ('Lose Game')
            continue
        # if the nimSum is 0, prints a loss and returns to start of loop

        indiNimSum=0
        # initializes individual nim sum
        
        for i in range (0,leng):
            indiNimSum=nimSum^intHeapList[i]
            # finds nimSum for each pair

            if indiNimSum<intHeapList[i]:
                removed=intHeapList[i]-indiNimSum
                print ('Remove',removed,'counters from Heap',i+1)
                break
            # if the individual nim sum < the current heap size, finds difference
            # between the 2 values and prints winning strategy then breaks out
            # of loop to start the next game
                                                  
    infile.close
    # closes file

main ()
