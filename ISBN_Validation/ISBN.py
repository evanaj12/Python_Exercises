#  File: ISBN.py

#  Description: Returns validity of potential ISBN numbers

#  Student Name: Evan Johnston

#  Student UT EID: eaj628

#  Course Name: CS 303E

#  Unique Number: 53590

#  Date Created: 11/9/13

#  Date Last Modified: 11/11/13

def main():
    inFile=open('isbn.txt','r')
    # opens the isbn file with the potential isbn numbers in read mode
    
    lineList=inFile.readlines()
    # assigns lineList to a list of all lines in the file
    
    line=inFile.readline()
    # assigns line to the read line in the file

    outFile=open('isbnOut.txt','w')
    # opens the file to which the outputs will be written
    
    validList=['0','1','2','3','4','5','6','7','8','9','x','X']
    # creates a list of all potential characters in a valid isbn number as strings
    # does not include '-' because '-' will be removed before
    # potential isbn number is tested
    
    for i in range (0,len(lineList)):
        # loop iterates for as many elements, or potential isbn numbers, are in the list
        
        line = lineList[i].rstrip ('\n')
        # removes newline character from each element
        
        original=line
        # preserves original potential isbn number
        
        line=list(line)
        # converts line to a list from string
            
        sum1=0
        sum2=0
        s1=[]
        s2=[]
        count=0
        flagIn=False
        flagLast=False
        # initialization of variables used below
    
        if line[-1]in validList:
            flagLast=True
            # tests if the last character of a potential isbn is
            # in the valid list of characters
        
        while '-' in line:
            line.remove('-')
            # removes all '-' from list

        
        for j in range (0,len(line)):
            #iterates for each character within the line (as a list) being tested
            
            if line[j] in validList:
                flagIn=True
                # tests if each character is in the valid list of characters
                
                if line[j]=='x':
                    line.remove('x')
                    line.insert(j,'10')
                    # finds all 'x' and replaces then with '10' as a str
                        
                if line[j]=='X':
                    line.remove('X')
                    line.insert(j,'10')
                    # finds all 'X' and replaces then with '10' as a str

                if (line[j] in validList) and (j<=len(line)-2):
                    count+=1
                    # now that all remaining characters in the list are numbers
                    # we count all the single digits (digits in the valid list)
                    # to make sure there are exactly 9 excluding the last character

                line[j]=int(line[j])
                # converts str digits to int
     
                sum1=sum1+line[j]
                # increments sum for each digit
                
                s1.append(sum1)
                # moves the cummulative sum to a list s1

                sum2=sum2+s1[j]
                # second round of summing
                
                s2.append(sum2)
                # moves the 2nd cummulative sum to the list s2
            else:
                # if the character is not a valid character, the loop breaks
                # and is directed to the invalid output
                s2=[0]
                break

        if (flagIn)and(flagLast)and(count==9)and(s2[-1]%11==0):
            print (original,'valid',file=outFile)
            # ensures all the potential isbn meets all requirements
            # writes output to output file
            
        else:
            print (original,'invalid',file=outFile)
            # if requirements are not met, invalid output written to file
            
    inFile.close
    outFile.close
    # closes both files

main()
