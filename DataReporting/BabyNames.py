#  File: BabyNames.py 

#  Description: Reads SSA file containing statistics on baby names in the US and performs
#  functions with the data

#  Student Name: Evan Johnston 

#  Student UT EID: eaj628 

#  Course Name: CS 313E

#  Unique Number: 53580

#  Date Created: 2/15/14

#  Date Last Modified: 2/21/14

import urllib.request

def menu():
    # function to call the menu list
    print ('Options:')
    print ('Enter 1 to search for names.')
    print ('Enter 2 to display data for one name.')
    print ('Enter 3 to display all names that appear in only one decade.')
    print ('Enter 4 to display all names that appear in all decades.')
    print ('Enter 5 to display all names that are more popular in every decade.')
    print ('Enter 6 to display all names that are less popular in every decade.')
    print ('Enter 7 to quit.')
    print ('')

def name(dic):
    # function that uses a loop to gather name input and put it in search form
    name=str(input('Enter a name: '))
    searchN=name.lower()
    if not (searchN in dic.keys()):
        return name
    else:
        searchN=name.lower()
        return searchN

def decade():
    # similar to the name function, but for decade input
    decade=int(input('Enter a decade: '))
    while not (1900<=decade<=2000):
        decade=int(input('Enter a decade: '))
    return decade

def name_in(name, dct):
    # returns name and most popular decade for that name
    names=list(dct.keys())
    if name in names:
        decades=dct.get(name)
    else:
        print (name+' does not appear in any decade.')
        return

    min=1002
    for i in range (11):
        if decades[i]<min:
            min=decades[i]
    idx1=decades.index(min)
    
    print ('The matches with their highest ranking decade are:')

    first=name[0].upper()
    name=first+name[1:]
    print (name, 1900+idx1*10)

def ranks(name, dct):
    # function that returns all the rankings for each decade for a given name.
    names=list(dct.keys())
    if name in names:
        decades=dct.get(name)
    else:
        print (name+' does not appear in any decade.')
        return
    
    first=name[0].upper()
    name=first+name[1:]
    decadeSt=''
    for i in range (11):
        if decades[i]==1001:
            decades[i]=0
        decadeSt+=str(decades[i])+' '

    print ('')
    print (name+': '+decadeSt)
    for i in range (11):
        print (str(1900+i*10)+': '+str(decades[i]))
    
def ranked_names_of_decade(decade, dct):
    # function that returns a list of names that have a rank in a specific decade
    if decade==2000:
        idx=10
    else:
        idx=(decade//10)%10
    decadeList=[]
    
    print ('The names are in alphabetical:')
    for i in range (len(dct)):
        if ((list(dct.values())[i])[idx])<1001:
            first=str(list(dct.keys())[i])[0].upper()
            name=first+str(list(dct.keys())[i])[1:]
            decadeList.append(name)
            
    decadeList.sort()
    for i in range (len(decadeList)):
        print (decadeList[i])
    
def all_decade_names(dct):
    # prints a list of all names that made the top 1000 list for every decade 1900-2000
    namesList=[]
    for i in range (len(dct)):
        flag=True
        for j in range (11):
            if 1001==(list(dct.values())[i])[j]:
                flag=False
        if flag: 
            first=str(list(dct.keys())[i])[0].upper()
            name=first+str(list(dct.keys())[i])[1:]
            namesList.append(name)
            
    namesList.sort()
    print (str(len(namesList))+' names appear in every decade. The names are: ')
    for i in range (len(namesList)):
        print (namesList[i])

def increasing_pop_names(dct):
    # function to display all names that are getting more popular in every decade.
    # The names must have a rank in all the decades to qualify. The output must be sorted by name.
    namesList=[]
    for i in range (len(dct)):
        flag=True
        for j in range (1,11):
            if 1001==(list(dct.values())[i])[j]:
                flag=False
                               
        if flag:
            countIncrease=0
            for k in range (1,11):
                if (list(dct.values())[i])[k]<(list(dct.values())[i])[k-1]:
                    countIncrease+=1
            if countIncrease==10:
                first=str(list(dct.keys())[i])[0].upper()
                name=first+str(list(dct.keys())[i])[1:]
                namesList.append(name)
                
    namesList.sort()
    print (str(len(namesList))+' names are more popular in every decade.')
    for i in range (len(namesList)):
        print (namesList[i])
    
def decreasing_pop_names(dct):
    # function to display all names that are getting less popular in every decade.
    # The names must have a rank in all the decades to qualify. The output must be sorted by name.
    namesList=[]
    for i in range (len(dct)):
        flag=True
        for j in range (10):
            if 1001==(list(dct.values())[i])[j]:
                flag=False
                
        if flag:
            countDecrease=0
            for k in range (1,11):
                if (list(dct.values())[i])[k]>(list(dct.values())[i])[k-1]:
                    countDecrease+=1
            if countDecrease==10:
                first=str(list(dct.keys())[i])[0].upper()
                name=first+str(list(dct.keys())[i])[1:]
                namesList.append(name)
                
    namesList.sort()
    print (str(len(namesList))+' names are less popular in every decade.')
    for i in range (len(namesList)):
        print (namesList[i])
            
def main():
    try:
        infile=urllib.request.urlopen('http://www.cs.utexas.edu/~mitra/csSpring2014/cs313/assgn/names.txt')
        tryFlag=True
    except OSError:
        # I am unsure of this is the correct exception Dr. Mitra was referring to, but
        # it works on my machine.
        infile=open ('names.txt', 'r')
        tryFlag=False
    finally:
        lines=infile.readlines()
        dic={}
    #reads in data from internet
    
    for i in range (len(lines)):
        if tryFlag:
            line = str (lines[i], encoding = 'utf8')
        else:
            line = str (lines[i])
        line=line.split()
        
        for i in range (1,len(line)):
            if line[i]=='0':
                line[i]=1001
            else:
                line[i]=int(line[i])
        
        line[0]=line[0].lower()
        dic [line[0]]=line[1:]
         
    menu()      
    choice=str(input('Enter choice: '))
    choiceList=['1','2','3','4','5','6']
        
    while choice in choiceList:

        if choice=='1':
            name_in(name(dic),dic)
            
        elif choice=='2':
            ranks(name(dic),dic)
            
        elif choice=='3':
            ranked_names_of_decade(decade(),dic)
            
        elif choice=='4':
            all_decade_names(dic)
            
        elif choice=='5':
            increasing_pop_names(dic)
            
        elif choice=='6':
            decreasing_pop_names(dic)           

        print ('')
        menu()      
        choice=str(input('Enter choice: '))
        
    if choice not in choiceList:
        print ('')
        print ('Goodbye.')
        return

    infile.close()
       
main()
