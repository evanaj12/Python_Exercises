#  File: Benford.py

#  Description: displays the frequency of how often each digit begins a set of data

#  Student Name: Evan Johnston

#  Student UT EID: eaj628

#  Course Name: CS 303E

#  Unique Number: 53590

#  Date Created: 11/27/13

#  Date Last Modified: 12/02/13

def main():
  pop_num = []
  inFile = open ("Census_2009.txt", "r")
  count = 0
  for line in inFile:
    if (count == 0):
      count += 1
      continue
    else:
      count += 1
      line = line.strip()
      word_list = line.split()
      pop_num.append (word_list[-1])
  inFile.close()
  # given code that reads in the data file, iterates a total count per line,
  # and strips the lines to a readable form

  count1=0
  count2=0
  count3=0
  count4=0
  count5=0
  count6=0
  count7=0
  count8=0
  count9=0
  # initiates count for each digit

  pop_dict={}
  # initiates dictionary for populations
  
  for i in range (len(pop_num)):
    leng=len(pop_num[i])
    first=int(pop_num[i])//(10**(leng-1))
    if first==1:
      count1+=1
    if first==2:
      count2+=1
    if first==3:
      count3+=1
    if first==4:
      count4+=1
    if first==5:
      count5+=1
    if first==6:
      count6+=1
    if first==7:
      count7+=1
    if first==8:
      count8+=1
    if first==9:
      count9+=1
    # loop iterates and adds to each count for each first digit 

  pop_dict [1]=count1
  pop_dict [2]=count2
  pop_dict [3]=count3
  pop_dict [4]=count4
  pop_dict [5]=count5
  pop_dict [6]=count6
  pop_dict [7]=count7
  pop_dict [8]=count8
  pop_dict [9]=count9
  # adds each count to the population dictionary

  digits=list(pop_dict.keys())
  freq=list(pop_dict.values())
  # creates list of just the keys, the digits, and the values, the frequencies
     
  perc1=round((count1/count)*100,1)
  perc2=round((count2/count)*100,1)
  perc3=round((count3/count)*100,1)
  perc4=round((count4/count)*100,1)
  perc5=round((count5/count)*100,1)
  perc6=round((count6/count)*100,1)
  perc7=round((count7/count)*100,1)
  perc8=round((count8/count)*100,1)
  perc9=round((count9/count)*100,1)
  # creates each relative frequency, based on count, rounded to 1 digit

  perc=[]
  perc.append(perc1)
  perc.append(perc2)
  perc.append(perc3)
  perc.append(perc4)
  perc.append(perc5)
  perc.append(perc6)
  perc.append(perc7)
  perc.append(perc8)
  perc.append(perc9)
  # adds each relative frequency to percent list

  print ('Digit'+' '*8+'Count'+' '*8+'%')
  for i in range (len(pop_dict)):
    print (str(digits[i])+' '*12+str(freq[i])+' '*10+str(perc[i]))
    # prints headers with 8 spaces between each and each category beneath
    # each column, relatively
 
main()
