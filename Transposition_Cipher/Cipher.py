#  File: Cipher.py

#  Description: uses a transposition cipher to encypt and decrypt input

#  Student Name: Evan Johnston

#  Student UT EID: eaj628

#  Partner Name: Carlos Brandon Ortiz

#  Partner UT EID: cbo268

#  Course Name: CS 303E

#  Unique Number:  53590

#  Date Created: 10/27/13

#  Date Last Modified:10/28/13


def main ():
  inp=str(input('Do you want to encrypt or decrypt? (E / D): '))
  print ('')
  #prompts user to decide if encryption or decryption will take place
  
  if inp=='E':
      #encryption process
      
      inFile=open('./input.txt','r')
      fileContent=inFile.read()
      #opens input.txt file in read mode
      
      leng=len(fileContent)
      #sets length of the read file to leng, for convenience 

      evenStr=''
      oddStr=''
      #initialize even and odd string variables
          
      for i in range (0,leng,2):
          evenStr=evenStr+fileContent[i]
          #creates a string of all the even characters in the read file
          
      for n in range (1,leng,2):
          oddStr=oddStr+fileContent[n]
          #creates a string of all the odd characters in the read file

      encryptedStr=oddStr+evenStr
      #combines the strings into a final encrypted string with the odd characters 1st
      #followed by the even characters
      
      inFile.close()
      #closes the read file

      outFile=open('./output.txt','w')
      outFile.write(encryptedStr)
      #opens the output.txt file in write mode, writing the encrypted string to it
      
      print ('Output written to output.txt')
      #printing where the results went

      outFile.close()
      #closes the written file
           
  elif inp=='D':
      #decryption process

      inFile=open('./input.txt','r')
      fileContent=inFile.read()
      #opens input.txt file in read mode
      
      leng=len(fileContent)
      #sets length of the read file to leng, for convenience

      decryptedStr=''
      #initialize decrypt string
      
      half=leng//2
      #defines half of the string

      oddStr=fileContent[:half]
      #the odd string is the first half of the input file content
      #so long as the input is encrypted with the same cipher

      evenStr=fileContent[half:]
      #the even string is the second half of the input file content
      #so long as the input is encrypted with the same cipher

      for i in range (0,half):
          decryptedStr=decryptedStr+evenStr[i]+oddStr[i]
          #the decrypted string increments and adds each even, then odd character

      inFile.close()
      #closes file
      
      if leng%2==0:
          #this applies to even inputs
        
          outFile=open('./output.txt','w')
          outFile.write(decryptedStr)
          #opens the output.txt file in write mode and writes the decrypted string there
          
          print ('Output written to output.txt')
          #printing where the results went
      
      else:
          #this applies to odd inputs
        
          outFile=open('./output.txt','w')
          outFile.write(decryptedStr+evenStr[-1])
          #opens the output.txt file in write mode and writes the decrypted string there
          #because of diffences in len() and index[], the last character
          #of the even string index[-1] is added to the output
          
          print ('Output written to output.txt')
          #printing where the results went

      outFile.close()
      #closes the written file
               
  else:
      print('Wrong input. Bye.')
      return
      #if the user does not input 'E' or 'D' this message is printed and the program exits.
    
main ()
