#  File: DNA.py

#  Description: Finds longest shared base sequence between 2 strands of DNA

#  Student Name: Evan Johnston

#  Student UT EID: eaj628

#  Course Name: CS 303E

#  Unique Number: 53590

#  Date Created: 10/31/13

#  Date Last Modified:11/1/13

def main():
    
    strand1=str(input('Enter first strand: '))
    strand2=str(input('Enter second strand: '))
    #prompts user for 2 strand sequences
    
    print ('')
    print ('Common Subsequence(s): ')
    #adds empty line followed by header
    
    flag=False
    #initializes flag for 'no common sequence' case
    

    if (len(strand1)>len(strand2)) or (len(strand1)==len(strand2)):
      #for all cases of a longer 1st strands or = length strands
        
      len_str = len(strand2)
      window = len_str
      #initialzes iterative variables in subsequence generating loops
      
      maxLen=0
      #initialzes maximum leng counter
      
      while (window > 0):
        startIndex = 0
        while (startIndex + window <= len_str):
          sub=strand2[startIndex : startIndex + window]
          #creation of nested while loop that generates all possible
          #substrings of the smaller strand
 
          if (sub in strand1):
                #conditional for subsequence in the longer strand

                firstCh=strand1.find(sub)
                #assigns 'firstCh' to the index of the first character in the longer
                #strand that is found (using find()) in the subsequence
                
                match=strand1[firstCh:firstCh+len(sub)]
                #assigns 'match' to the string between 'firstCh' and
                #'firstCh+length of substring'
                
                if len(match)>=maxLen and len(match)>1:
                    #conditional to set 'maxLen' to the longest matched string
                    #so long as it is more than 1 character

                    maxLen=len(match)
                    print (match)

                    flag=True
                    #flag set to 'True' to stop 'no common sequence' case from occuring
                      
                      
          startIndex += 1
        window = window - 1
        #iterates variables of the substring generator loop
        
      if flag!=True:
            print ('No Common Sequence Found.')
            #if flag remains 'False' then 'no common sequence' case is printed

    elif len(strand2)>len(strand1):
      #same as above section with strand lengths reversed
                              
      len_str = len(strand1)
      window = len_str
      maxLen=0
      
      while (window > 0):
        startIndex = 0
        
        while (startIndex + window <= len_str):
          sub=strand1[startIndex : startIndex + window]
 
          if (sub in strand2):
                firstCh=strand2.find(sub)
                match=strand2[firstCh:firstCh+len(sub)]
                
                if len(match)>=maxLen and len(match)>1:
                      maxLen=len(match)
                      print (match)
                      flag=True
                      
          startIndex += 1
        window = window - 1
        
      if flag!=True:
            print ('No Common Sequence Found.')
        
main()
    

