#  File: TestSparseMatrix.py

#  Description: Sparse matrix representation has a single linked list
#               having the row, column, and non-zero data in each link

#  Student Name: Evan Johnston

#  Student UT EID: eaj628

#  Course Name: CS 313E

#  Unique Number: 53580

#  Date Created: 4/4/14

#  Date Last Modified: 4/5/14

class Link (object):
  def __init__ (self, row = 0, col = 0, data = 0, next = None):
    self.row = row
    self.col = col
    self.data = data
    self.next = next

  # returns a String representation of a Link (row, col, data)
  def __str__ (self):
    s=str(self.data)
    return s

class LinkedList (object):
  def __init__ (self):
    self.first = None

  def insertLast (self, row, col, data):
    newLink = Link (row, col, data)
    current = self.first

    if (current == None):
      self.first = newLink
      return

    while (current.next != None):
      current = current.next

    current.next = newLink

  def __len__ (self):
    count=0
    current=self.first
    while current!=None:
      count+=1
      current=current.next

    return count

  # returns a String representation of a LinkedList
  def __str__ (self):
    s=''
    current=self.first
    while current!=None:
      s+=str(current)+' '
      current=current.next
      
    return s

  # returns a new list with all zeros removed
  def remove_Zeros (self):
    current=self.first
    newList=LinkedList()
    
    while current!=None:
      if current.data!=0:
        newList.insertLast(0,0,current.data)
      current=current.next

    return newList
  # I used this function to remove zeros instead of the get row
  # and get col functions because I used those functions in
  # the mutliplication and clearing the zeros in them would not
  # allow that

class Matrix (object):
  def __init__ (self, row = 0, col = 0):
    self.row = row
    self.col = col
    self.matrix = LinkedList()
  
  # finds the Link having row and col value
  def find (self, row, col):
    if row>self.row or col>self.col:
      return None
    # if the search is out of bound returns none
    
    current=self.matrix.first
    previous=current
    
    for i in range (self.col*(row)+col):
      # iterates for the total number of columns*the searched row
      # to reach the appropriate row, then + the searched column
      # to reach the final destination
      previous=current
      current=current.next

    return current

  # removes the Link having row and col value
  def delete (self, row, col):
    # similar to find function
    
    if row>self.row or col>self.col:
      return None
    
    if row==0 and col==0:
      self.matrix.first=self.matrix.first.next
      # if the first position is being deleted, shifts matrix by 1
      return
    
    current=self.matrix.first
    previous=current
    
    for i in range (self.col*(row)+col):
      previous=current
      current=current.next
      
    current=current.next
    previous.next=current
  
  # Performs assignment operation:  matrix[row][col] = data
  def set_element (self, row, col, data):
    # similar to find and delete functions
    
    newLink=Link(row,col,data)
    
    if row>self.row or col>self.col:
      return None
    
    if row==0 and col==0:
      self.matrix.first.data=data
      return
      
    current=self.matrix.first
    previous=current
    
    for i in range (self.col*(row)+col):
      previous=current
      current=current.next
      
    previous.next=newLink
    newLink.next=current.next

  # Adds two sparse matrices 
  def __add__ (self, other):
    
    if self.row!=other.row and self.col!=other.col:
      return None
    
    newMatrix=Matrix(self.row,self.col)
    currentA=self.matrix.first
    currentB=other.matrix.first
      
    for i in range (self.row):
      for j in range (self.col):
        newData=currentA.data+currentB.data
        # adds each data from same spots from each matrix
        
        newMatrix.matrix.insertLast(i,j,newData)
            
        currentA=currentA.next
        currentB=currentB.next

    return newMatrix

  # Multiplies two sparse matrices 
  def __mul__ (self, other):
    m=self.row
    n=self.col
    o=other.row
    p=other.col

    if (n!=o):
      return None
    # returns none if the matricies are incompatible for multiplication
    
    newMatrix=Matrix(m,p)
    
    for i in range (m):
      rowsA=self.getRow(i)
      # each iteration of i creates a new rowlist
      # from the first matrix
      
      for j in range (p):
        colsB=other.getCol(j)
        # each iteration of j creates a new collist
        # from the second matrix
        
        currentA=rowsA.first
        currentB=colsB.first
        sum=0
        
        for k in range (n):
          # each iteration of k finds the product of the 2
          # current data of the matrices
          # and adds them to the sum for that iteration of j
          product=currentA.data*currentB.data
          sum+=product
          
          currentA=currentA.next
          currentB=currentB.next

        newMatrix.matrix.insertLast(i,j,sum)
        # adds to the new matrix the sum and clears the sum on the
        # next iteration of j

    return newMatrix
  
  # Returns a linked list representing a row
  def getRow (self, n):
    rows=self.row
    cols=self.col
    current=self.matrix.first
    newList=LinkedList()

    if n>rows:
      return None
    # returns none if the requested row is out of bounds

    for i in range (cols*n):
      current=current.next
      # iterates to put current at appropriate row
      
    for i in range (cols):
      newList.insertLast(n,i,current.data)
      # adds row to new list for the duration of the number of cols
      current=current.next

    return newList

  # Returns a linked list representing a column
  def getCol (self, n):
    # similar to get rows
    
    rows=self.row
    cols=self.col
    current=self.matrix.first
    newList=LinkedList()

    if n>cols:
      return None
    # returns none if the requested column is out of bounds

    for i in range (n):
      current=current.next

    newList.insertLast(1, n, current.data)
    # inserts first data of the column

    count=0
    # counts to keep track of the current position
    # after the first data has been added, every time the
    # cursor moves the total number of columns, it has returned
    # to the target column and adds that data to the new list
    for i in range (rows*cols-n-1):
      count+=1
      current=current.next
      if count==cols:
        newList.insertLast(i, n, current.data)
        count=0

    return newList
  
  # Returns a string representation of a matrix
  def __str__ (self):
    row=self.row
    col=self.col
    matrix=self.matrix
    s=''
    current=matrix.first
    
    for i in range (row):
      count=0
      for j in range (col):
        if current==None:
          s+='{:>4}'.format(' ')
        elif count==col-1:
          s+='{:>4}'.format(current.data)+'\n'
          current=current.next
        else:
          s+='{:>4}'.format((current.data))
          count+=1
          current=current.next
        
    return s

def readMatrix (inFile):
  line = inFile.readline().rstrip("\n").split()
  row = int (line[0])
  col = int (line[1])
  mat = Matrix (row, col)

  for i in range (row):
    line = inFile.readline().rstrip("\n").split()
    for j in range (col):
      elt = int(line[j])
      mat.matrix.insertLast (i, j, elt)
  line = inFile.readline()

  return mat

def main ():
  inFile = open ("matrix.txt", "r")

  print ("Test Matrix Addition")
  matA = readMatrix (inFile)
  print (matA)
  matB = readMatrix (inFile)
  print (matB)

  matC = matA + matB
  print (matC)

  print ("\nTest Matrix Multiplication")
  matP = readMatrix (inFile)
  print (matP)
  matQ = readMatrix (inFile)
  print (matQ)
  
  matR = matP * matQ
  print (matR)

  print ("\nTest Setting a Zero Element to a Non-Zero Value")
  matA.set_element (1, 1, 5)
  print (matA)

  print ("\nTest Getting a Row")
  row = matP.getRow(1)
  row = row.remove_Zeros()
  print (row)

  print ("\nTest Getting a Column")
  col = matQ.getCol(0)
  col = col.remove_Zeros()
  print (col)

  inFile.close()

main()
