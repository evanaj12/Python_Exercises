#  File: WordSearch.py

#  Description: Completes a wordsearch with given words and puzzle.

#  Student Name: Evan Johnston

#  Student UT EID: eaj628

#  Partner Name: Carlos Brandon Ortiz

#  Partner UT EID: cbo268

#  Course Name: CS 303E 

#  Unique Number: 53590

#  Date Created: 11/11/13

#  Date Last Modified: 11/15/13

def string_rows (b):
  for row in b:
    s = ''
    for col in row:
      s += str(col)
    return (s)
  #function returns rows in a 2D list as strings

def reverse_st(s):
    newS=''
    for i in range (len(s)-1,-1,-1):
      newS+=s[i]
    return newS
  #returns the reverse of a string in a new string

def main():
    inFile=open('hidden.txt','r')
    outFile=open('found.txt','w')
    #opens the input and output files in read and write mode, respectively
    
    lineList=inFile.readlines()
    #creates a list with each line of input as an element

    dimensions=(lineList[0]).split()
    m=int(dimensions[0])
    n=int(dimensions[1])
    #finds the dimensions of the wordsearch, m is the number of rows, n is columns

    fullList=lineList[2:m+2]
    #creates a list that is just the wordsearch matrix
    
    twoDlist=[]
    for i in range(len(fullList)):
        line=list(fullList[i])
        while ' ' in line:
            line.remove(' ')
        while '\n' in line:
            line.remove('\n')
        twoDlist.append(line)
    #creates 2-D list of the wordsearch, removing all extraneous characters
    
    wordread=lineList[m+4:]
    if '\n' in wordread:
      wordread.remove('\n')
    wordList=[]
    for i in range (len(wordread)):
        word=(wordread[i]).rstrip()
        wordList.append(word)
    wordForward=wordList
    k2=len(wordForward)
    #creates list with all words from the list, and preserves it in wordForward
    
    for i in range (len(wordList)):
        revList=reverse_st(wordList[i])
        wordList.append(revList)
    #creates a list with all possible words, including the reverse, in wordList

    k=len(wordList)

    noneList=[]
    #initializes the list of words found in the wordsearch

    foundList=[]
    #list to be used with found words and values to return original order

    counti=1
    #counti starts the count that will be the row of the found words
    
    for i in range (m):
        row=string_rows(twoDlist[i:])
        #creates row for each element of the 2-D list, which is a row of the wordsearch

        for j in range (k):
            indexRStart=row.find(wordList[j])
            #finds each word in wordList in each row
            
            if (j>k2) and (indexRStart!=-1):
                #True if the word is found and it is backwards
              
                positionx= len(wordList[j])+indexRStart
                #forms the found word with the index from the find function
                #adds it backwards as the word needs to be counted from its begining character
                
                fixedWordx=reverse_st(wordList[j])
                #faces the word in the correct direction again
                
                foundList.append(fixedWordx)
                foundList.append(counti)
                foundList.append(positionx)
                #appends each word and value to list that will reorder them
                

                noneList.append(fixedWordx)
                #adds the word to the list of found words

            if (indexRStart!=-1) and (j<=m):
                #True if the word is found and it is forwards
              
                positionx= indexRStart+1
                #print (wordList[j]+'  '+str(counti)+'  '+str(positionx), file=outFile)
                noneList.append(wordList[j])
                foundList.append(wordList[j])
                foundList.append(counti)
                foundList.append(positionx)
                #same as above process

        counti+=1
                         
    countj=1
    #counti starts the count that will be the row of the found words

    for j in range (len(twoDlist[0])):
      col=''
      for i in range (m):
         col+=str(twoDlist[i][j])
         #these loops create each column of the 2-D list as string
         
      for p in range (k):
          indexStart=col.find(wordList[p])
          #finds word in each column
          
          if (p>n) and (indexStart!=-1):
              positiony= len(wordLists[p])+indexStart
              fixedWordy=reverse_st(wordList[j])
              noneList.append(fixedWordy)
              foundList.append(fixedWordy)
              foundList.append(countj)
              foundList.append(positiony)
              #same process as with rows

              
          if indexStart!=-1 and j<=m:
              positiony= indexStart+1
              noneList.append(wordList[p])
              foundList.append(wordList[p])
              foundList.append(countj)
              foundList.append(positiony)
              #same process as with rows

      countj+=1
      
    for i in range (k2):
      if not(wordList[i] in noneList):
          positionx=0
          counti=0
          #iterates for each word in wordList and if it is not in the compiled list
          #returns position 0 0
          foundList.append(wordList[i])
          foundList.append(counti)
          foundList.append(positionx)
          #same process as above
          
    for i in range (k2):
      for j in range (0,len(foundList),3):
        if foundList[j]==wordForward[i]:
          out=foundList[j:j+3]
          print ('%-11s' % out[0], '%2d' % out[1], '%3d' % out[2], file=outFile)
          #prints output in the oringal order in the outfile
          

main()
