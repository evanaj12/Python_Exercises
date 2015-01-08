# File: TestDenseMatrix.py

# Description: Matrix is represented as 2-D list

#  Student Name: Evan Johnston

#  Student UT EID: eaj628

#  Course Name: CS 313E

#  Unique Number: 53580

#  Date Created: 4/4/14

#  Date Last Modified: 4/5/14

class Matrix (object):
  def __init__ (self, row = 0, col = 0):
    self.row = row
    self.col = col
    self.matrix = []

  # performs a matrix addition
  def __add__ (self, other):
    if ((self.row != other.row) or (self.col != other.col)):
      return None

    mat = Matrix(self.row, self.col)
    for i in range (self.row):
      new_row = []
      for j in range (self.col):
        new_row.append (self.matrix[i][j] + other.matrix[i][j])
      mat.matrix.append(new_row)

    return mat

  # performs a matrix multiplication
  def __mul__ (self, other):
    if (self.col != other.row):
      return None

    mat = Matrix (self.row, other.col)
    for i in range (self.row):
      new_row = []
      for j in range (other.col):
        sum = 0
        for k in range (other.row):
          sum = sum + self.matrix[i][k] * other.matrix[k][j]
        new_row.append (sum)
      mat.matrix.append (new_row)

    return mat

  # returns a string representation of the matrix
  def __str__ (self):
    row=self.row
    col=self.col
    matrix=self.matrix
    s=''
    
    for i in range (row):
      count=0
      for j in range (col):
        if count==col-1:
          s+='{:>3}'.format((matrix[i][j]))+'\n'
        else:
          s+='{:>3}'.format((matrix[i][j]))
          count+=1

    return s

def readMatrix(inFile):
  line = inFile.readline().rstrip("\n").split()
  row = int(line[0])
  col = int(line[1])
  mat = Matrix(row, col)

  for i in range (row):
    line = inFile.readline().rstrip("\n").split()
    for j in range (col):
      line[j] = int(line[j])
    mat.matrix.append(line)
  line = inFile.readline()
  
  return mat

def main():
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

  inFile.close()

main()
