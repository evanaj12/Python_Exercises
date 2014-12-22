#  File: TestCipher.py

#  Description:encrypts and decrypts text in a substitution and Vigenere cipher

#  Student's Name:Evan Johnston

#  Student's UT EID:eaj628

#  Course Name: CS 313E 

#  Unique Number: 53580

#  Date Created:1/22/14

#  Date Last Modified:1/23/14

def substEn(strng):
    # substitution encryption function
    
    strng=strng.lower()
    # makes all letters in string lowercase
    
    alpha='abcdefghijklmnopqrstuvwxyz' 
    cipherText='qazwsxedcrfvtgbyhnujmikolp'
    # alphabet of lowercase letters and the given cipher alphabet

    encoded=''
    # initializes encrypted string
    
    for i in range (0,len(strng)):
        # iterates for length of string
        
        if strng[i] in alpha:
            # separates lowercase letters from all other characters
            
            idx=ord(strng[i])-ord('a')
            # index is the difference of the ordinal number of the character
            # and the ordinal number of 'a'
            
            encoded+=cipherText[idx]
            # adds the cipher character of the calculated index to the encrypted string
 
        else:
            encoded+=strng[i]
            # if the character is not a lowercase leter, adds the character to the
            # encrypted string
 
    return (str(encoded))
        
def substDe(strng):
    # substitution decryption function
    # code is similar to encryption function above

    alpha='abcdefghijklmnopqrstuvwxyz'
    cipherText='qazwsxedcrfvtgbyhnujmikolp'

    decoded=''
    for i in range (0,len(strng)):
        if strng[i] in alpha:
            idx=cipherText.find(strng[i])+ord('a')
            # index is the index of the character in the cipher (of which there is
            # only 1 of each character in the cipher) + the ordinal number of 'a' (97)
            
            decoded+=chr(idx)
            # character of the index based on ASCII value adds to decoded string
            
        else:
            decoded+=strng[i]

    return (str(decoded))

def vigEn (strng,passwd):
    # Vigenere cipher encryption function
    
    strng=strng.lower()
    alpha='abcdefghijklmnopqrstuvwxyz'       
    lengText=len(strng)
    encoded=''
    
    while len(passwd)<lengText:
        passwd+=passwd
        # while the length of the password is less than the length of the text
        # adds the password to the original. This ensures that the password will
        # eventually be as long as, probably longer than, the string.

    for i in range(0,lengText):
        if strng[i] in alpha:
            idxStrng=alpha.find(strng[i])
            # finds the index of the character in the alpha string (of which
            # there is only 1 of each character)
            
            shiftAlpha=(alpha[idxStrng:]+alpha[:idxStrng])
            # creates string of the shifted alphabet based on the found index
            
            idxPass=alpha.find(passwd[i])
            # finds index of the character of the password that corresponds to the
            # character of the string in the alpha string
            
            encoded+=shiftAlpha[idxPass]
            # adds character from the shifted alphabet with the password index
            
        else:
            encoded+=strng[i]
            passwd=passwd[:i]+strng[i]+passwd[i:]
            # if there are non-letter characters in the string, adds those characters
            # to the password to maintain the length and alignment of the characters
            
    return encoded
       
def vigDe (strng,passwd):
    # Vigenere cipher decryption function

    alpha='abcdefghijklmnopqrstuvwxyz'
    lengText=len(strng)
    decoded=''

    while len(passwd)<lengText:
        passwd+=passwd

    for i in range(0,lengText):
        if strng[i] in alpha:
            idxPass=alpha.find(passwd[i])
            # finds the index of password character in the alphabet
                        
            shiftAlpha=(alpha[idxPass:]+alpha[:idxPass])
            idxStrng=shiftAlpha.find(strng[i])
            # same process of shifting and finding the index, but with the password
            # then the string rather than vice-versa
            
            decoded+=alpha[idxStrng]
            # adds character from the alphabet rather than the shifted alphabet with
            # the string index in place of the password index
            
        else:
            decoded+=strng[i]
            passwd=passwd[:i]+strng[i]+passwd[i:]

    return decoded

def main():
    
    print('Substitution Cipher')
    print ('')

    subsTextEn=str(input('Enter Plain Text to be Encoded: '))
    print ('Encoded Text:',substEn(subsTextEn))
    print ('')

    subsTextDe=str(input('Enter Encoded Text to be Decoded: '))
    print ('Decoded Plain Text:',substDe(subsTextDe))
    print ('')

    print('Vigenere Cipher')
    print ('')

    vigTextEn=str(input('Enter Plain Text to be Encoded: '))
    vigEnPass=str(input('Enter Pass Phrase (no spaces allowed): '))
    print('Encoded Text:',vigEn(vigTextEn,vigEnPass))
    print ('')

    vigTextDe=str(input('Enter Encoded Text to be Decoded: '))
    vigDePass=str(input('Enter Pass Phrase (no spaces allowed): '))
    print('Decoded Plain Text:',vigDe(vigTextDe,vigDePass))

main()
