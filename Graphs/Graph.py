#  File: Graph.py

#  Description: Creates a tests a graph class

#  Student Name: Evan Johnston

#  Student UT EID: eaj628

#  Course Name: CS 313E

#  Unique Number: 53580

#  Date Created: 4/24/14

#  Date Last Modified: 5/5/14

#####################################################################

class Stack (object):
  def __init__ (self):
    self.stack = []

  # add an item to the top of the stack
  def push (self, item):
    self.stack.append ( item )

  # remove an item from the top of the stack
  def pop (self):
    return self.stack.pop()

  # check what item is on top of the stack without removing it
  def peek (self):
    return self.stack[len(self.stack) - 1]

  # check if a stack is empty
  def isEmpty (self):
    return (len(self.stack) == 0)

  # return the number of elements in the stack
  def size (self):
    return (len(self.stack))

  def __str__ (self):
    return str(self.stack)

class Queue (object):
  def __init__ (self):
    self.queue = []

  def enqueue (self, item):
    self.queue.append (item)

  def dequeue (self):
    return (self.queue.pop(0))

  def isEmpty (self):
    return (len (self.queue) == 0)

  def size (self):
    return len (self.queue)

  def __str__ (self):
    return str(self.queue)

class Vertex (object):
  def __init__ (self, label):
    self.label = label
    self.visited = False

  # determine if vertex was visited
  def wasVisited (self):
    return self.visited

  # determine the label of the vertex
  def getLabel (self):
    return self.label

  # string representation of the vertex
  def __str__ (self):
    return str (self.label)

class Edge (object):
  def __init__ (self, fromVertex, toVertex, weight):
    self.u = fromVertex
    self.v = toVertex
    self.weight = weight

  # comparison operators
  def __lt__ (self, other):
    return self.weight<other.weight

  def __le__ (self, other):
    return self.weight<=other.weight

  def __gt__ (self, other):
    return self.weight>other.weight

  def __ge__ (self, other):
    return self.weight>=other.weight

  def __eq__ (self, other):
    return self.weight==other.weight

  def __ne__ (self, other):
    return self.weight!=other.weight

class Graph (object):
  def __init__ (self):
    self.Vertices = []
    self.adjMat = []

  # returns a string representation of the adjacency matrix
  def printAdjMat (self):
    nVert=len(self.Vertices)
    matrix=self.getAdjMat()
    s=''
    
    for i in range (nVert):
      count=0
      for j in range (len(self.adjMat)):
        if count==nVert-1:
          s+='{:>3}'.format((matrix[i][j]))+'\n'
        else:
          s+='{:>3}'.format((matrix[i][j]))
          count+=1
    print (s)

  # check if a vertex already exists
  def hasVertex (self, label):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if (label == (self.Vertices[i]).label):
        return True
    return False

  # add a vertex with a given label
  def addVertex (self, label):
    if not self.hasVertex (label):
      self.Vertices.append (Vertex (label))
    
      # add a new column in the adjacency matrix for the new Vertex
      nVert = len (self.Vertices)
      for i in range (nVert - 1):
        (self.adjMat[i]).append (0)
 
      # add a new row for the new Vertex in the adjacency matrix
      newRow = []
      for i in range (nVert):
        newRow.append (0)
      self.adjMat.append (newRow)
      
  # add weighted directed edge to graph
  def addDirectedEdge (self, start, finish, weight = 1):
    self.adjMat[start][finish] = weight

  # add weighted undirected edge to graph
  def addUndirectedEdge (self, start, finish, weight = 1):
    self.adjMat[start][finish] = weight
    self.adjMat[finish][start] = weight
    
  # return an unvisited vertex adjacent to vertex v
  def getAdjUnvisitedVertex (self, v):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if (self.adjMat[v][i] > 0) and (not (self.Vertices[i]).wasVisited()):
        return i
    return -1

  # given a label get the index
  def getIndex (self, label):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if ((self.Vertices[i]).getLabel() == label):
        return i
    return -1

  # returns if an edge is directed or not
  def isDirectedEdge (self, fromVertexLabel, toVertexLabel):
    if self.getEdgeWeight(fromVertexLabel, toVertexLabel)>0:
      
      idx1=self.getIndex(fromVertexLabel)
      idx2=self.getIndex(toVertexLabel)
      
      if self.adjMat[idx1][idx2]==self.adjMat[idx2][idx1]:
        return False
      
      return True
    
  # returns if a graph is directed or not (only needs 1 directed edge to be directed)
  def isDirectedGraph (self):
    nVert=len(self.Vertices)
    for i in range (nVert):
      row=self.adjMat[i]
      col=[]
      for j in range (len(self.adjMat)):
        col.append(self.adjMat[j][i])
      if col!=row:
        return True
    return False

  # do a depth first search in a graph
  def dfs (self, v):
    # create a stack
    theStack = Stack()

    # mark the vertex as visited and push on the stack
    (self.Vertices[v]).visited = True
    print (self.Vertices[v])
    theStack.push (v)

    while (not theStack.isEmpty()):
      # get an adjacent unvisited vertex
      u = self.getAdjUnvisitedVertex (theStack.peek())
      if (u == -1):
        u = theStack.pop()
      else:
        (self.Vertices[u]).visited = True
        print (self.Vertices[u])
        theStack.push (u)

    # the stack is empty, reset the flags
    nVert = len (self.Vertices)
    for i in range (nVert):
      (self.Vertices[i]).visited = False

  # do a breadth first search in the graph
  def bfs (self, v):
    # create a queue
    theQueue = Queue()

    # mark the vertex as visited and enqueue
    (self.Vertices[v]).visited = True
    print (self.Vertices[v])
    theQueue.enqueue (v)

    while (not theQueue.isEmpty()):
      # get the vertex at the front
      v1 = theQueue.dequeue()
      # get an adjacent unvisited vertex
      v2 = self.getAdjUnvisitedVertex (v1)
      while (v2 != -1):
        (self.Vertices[v2]).visited = True
        print (self.Vertices[v2])
        theQueue.enqueue (v2)
        v2 = self.getAdjUnvisitedVertex (v1)

    # queue is empty, reset the flags
    nVert = len (self.Vertices)
    for i in range (nVert):
      (self.Vertices[i]).visited = False
    
  # get edge weight between two vertices
  # return -1 if edge does not exist
  def getEdgeWeight (self, fromVertexLabel, toVertexLabel, adjMat):
      if self.hasVertex(fromVertexLabel) and self.hasVertex(toVertexLabel):
        a=self.getIndex(fromVertexLabel)
        b=self.getIndex(toVertexLabel)
        
        if adjMat[a][b]>0:
          return adjMat[a][b]
        else:
          return -1
      else:
        return -1
        
  # get a list of neighbors that you can go to from a vertex
  # return empty list if there are none
  # in a directed graph this shows neighbors in the child direction (outgoing)
  # not parent (incoming)
  def getNeighbors (self, vertexLabel, copy):
      neighbors=[]
      nVert=len(self.Vertices)
      
      for i in range (nVert):
        possibleNeighbor=self.Vertices[i].label
        
        if self.getEdgeWeight(vertexLabel, possibleNeighbor, copy)>0:
          neighbors.append(possibleNeighbor)
          
      return neighbors

  # gets list of incoming edges in a directed graph
  def getIncoming (self, vertexLabel, adjMat):
    if self.isDirectedGraph():
      incoming=[]
      nVert=len(self.Vertices)
      idx=self.getIndex(vertexLabel)

      for i in range (nVert):
        if adjMat[i][idx]!=0:
          incoming.append(self.Vertices[i].label)

      return incoming
          
  # get a copy of the list of vertices
  def getVertices (self):
      nVert=len(self.Vertices)
      copy=[]
      
      for i in range (nVert):
        copy.append(self.Vertices[i].label)
        
      return copy
    
  # get a copy of the adjacency matrix
  def getAdjMat (self):
      nVert=len(self.Vertices)
      copy=[]

      for i in range (nVert):
        copy.append(list(self.adjMat[i]))

      return copy
    
  # gets a 2D list of edges in the form [weight, from Vertex, to Vertex]
  def getEdges(self):
      nVert=len(self.Vertices)
      edges=[]

      for i in range (nVert):
        for j in range (len(self.adjMat)):
          individual=[]
          if self.adjMat[i][j]!=0:
            individual.append(self.adjMat[i][j])
            individual.append(self.Vertices[i].label)
            individual.append(self.Vertices[j].label)
          edges.append(individual)

      while [] in edges:
        edges.remove([])

      return (edges)
        
  # determine if the graph has a cycle
  # uses modified DFS
  def hasCycle (self, copy):
    nVert=len(self.Vertices)
    v=0
    # starts from first vertex
    
    # create a stack
    theStack = Stack()

    # mark the vertex as visited and push on the stack
    (self.Vertices[v]).visited = True
    #print (self.Vertices[v])
    theStack.push (v)

    while (not theStack.isEmpty()):
      # get an adjacent unvisited vertex
      u = self.getAdjUnvisitedVertex (theStack.peek())

      n = theStack.peek()
      nLab=self.Vertices[n].label
      # n is the previous, 'parent', vertex visited (top of the stack)
      
      if u!=-1:
        uLab=self.Vertices[u].label
        for i in range (theStack.size()):
          comparisonLab=self.Vertices[theStack.stack[i]].label
          
          # looks through stack and compares each visited vertex
          # if it is visited, and therefore in the stack, and is not the parent
          # then a cycle exists
          if self.getEdgeWeight(uLab,comparisonLab, copy)>0 and comparisonLab!=nLab:
            return True
          
      if (u == -1):
        u = theStack.pop()
      else:
        (self.Vertices[u]).visited = True
        #print (self.Vertices[u])
        theStack.push (u)

    # the stack is empty, reset the flags
    nVert = len (self.Vertices)
    for i in range (nVert):
      (self.Vertices[i]).visited = False
      
    # if no cycle was found, returns false     
    return False

  # returns if a Vertex is a leaf in a directed graph, meaning it has no
  # sucessor vertex
  def isLeaf (self, VertexLabel):
    if self.isDirectedGraph:
      idx=self.getIndex(VertexLabel)
      
      for i in range (len(self.adjMat[idx])):
        if self.adjMat[idx][i]!=0:
          return False
        
      return True
    
  # return a list of vertices after a topological sort
  def toposort (self):
      # list that contains sorted elements
      topo=[]
      # queue that contains nodes with no incoming edges
      leaves=Queue()
      nVert=len(self.Vertices)

      # creates copy of the adjacency matrix to preserve the original
      copy=self.getAdjMat()

      for i in range (nVert):
        # builds leaves queue
        if len(self.getIncoming(self.Vertices[i].label, copy))==0:
          leaves.enqueue(self.Vertices[i])

      while not(leaves.isEmpty()):
        v=leaves.dequeue().label
        topo.append(v)
        neighbors=self.getNeighbors(v, copy)
        # list of neighbors of v
        
        for i in range (len(neighbors)):
          # deletes edge from v to any neighbor in the copy
          self.deleteEdge(v, neighbors[i], copy)

          # if the neighbor also has no incoming edges, appends to leaves
          if len(self.getIncoming(neighbors[i], copy))==0:
            idx=self.getIndex(neighbors[i])
            leaves.enqueue(self.Vertices[idx])
            
      return topo
                 
  # prints a list of edges for a minimum cost spanning tree
  # list is in the form [v1 - v2, v2 - v3, ..., vm - vn]
  def spanTree (self, startIndex):
    if (self.isDirectedGraph()==False):
      copy=self.getAdjMat()
      nVerts=len(self.Vertices)

      # sorts edge list in ascending order of weight
      sortedEdges=sorted (self.getEdges())
      span=Stack()
      doubles=[]
      tree=Graph()

      # removes doubles from list (when from->to==to->from)
      for i in range (len(sortedEdges)):
        trial=sortedEdges[i]
        trial[1],trial[2]=trial[2],trial[1]
        if sortedEdges.count(trial)>1:
          doubles.append(trial)

      for i in range (len(doubles)):
        sortedEdges.remove(doubles[i])

      # creates new graph that is the min-cost-spanning tree
      for i in range (nVerts):
        tree.addVertex(self.Vertices[i].label)
       
      for i in range (len(sortedEdges)):
        tree.addUndirectedEdge(self.getIndex(sortedEdges[i][1]),\
                self.getIndex(sortedEdges[i][2]),sortedEdges[i][0])

        span.push(sortedEdges[i][1]+' - '+sortedEdges[i][2])
        if tree.hasCycle(tree.adjMat):
          span.pop()
          tree.deleteEdge(sortedEdges[i][1],sortedEdges[i][2],tree.adjMat)
          tree.deleteEdge(sortedEdges[i][2],sortedEdges[i][1],tree.adjMat)
          
      return span.stack
                       
  # determine shortest path from a single vertex
  def shortestPath (self, fromVertexLabel):
    dist=[]
    for i in range (len(self.Vertices)):
      dist.append(None)
    dist[0]=0
    copy=self.adjMat

    firstNeighbors=self.getNeighbors(fromVertexLabel, copy)
    min=999999999
    
    for i in range (len(firstNeighbors)):
      weight=self.getEdgeWeight(fromVertexLabel, firstNeighbors[i], copy)
      if weight<=min:
        weight=min
        idx=self.getIndex(firstNeighbors[i])
        if not(self.Vertices[idx].visited):
          choice=self.Vertices[idx]

    for i in range (len(self.Vertices)):
      print (str(self.Vertices[i])+' - '+str(dist[i]))
          
  # delete an edge from the adjacency matrix
  # note that this only deletes the edge in 1 direction
  # adjMat parameter is to preserve original adjacency matrix
  def deleteEdge (self, fromVertexLabel, toVertexLabel, adjMat):
    if self.getEdgeWeight(fromVertexLabel, toVertexLabel, adjMat)!=0:
      idx1=self.getIndex(fromVertexLabel)
      idx2=self.getIndex(toVertexLabel)

      adjMat[idx1][idx2]=0

  # delete a vertex from the vertex list and all edges from and
  # to it in the adjacency matrix
  # adjMat and verts parameters are to preseve the orginal attributes
  def deleteVertex (self, vertexLabel, verts, adjMat):
    nVert=len(self.Vertices)
    idx=self.getIndex(vertexLabel)
    
    copyV=self.getVertices()
    copyA=self.getAdjMat()

    for i in range (nVert):
      # removes the respective column aspect of the adjcency matrix
        adjMat[i].pop(idx)
      
    # removes the respective row from the adjcency matrix
    adjMat.pop(idx)
    
    # removes the label from the vertices list
    verts.pop(idx)
    
def main():
  # Create Graph object
  graph = Graph()

  # Open file for reading
  inFile = open ("./graph5.txt", "r")

  # Read the vertices
  numVertices = int ((inFile.readline()).strip())

  for i in range (numVertices):
    city = (inFile.readline()).strip()
    graph.addVertex (city)

  # Read the edges
  numEdges = int ((inFile.readline()).strip())

  for i in range (numEdges):
    edge = (inFile.readline()).strip()
    edge = edge.split()
    start = int (edge[0])
    finish = int (edge[1])
    weight = int (edge[2])
    graph.addDirectedEdge (start, finish, weight)

  # Read the starting vertex for dfs, bfs, and shortest path
  startVertex = (inFile.readline()).strip()

  # Close file
  inFile.close()

  startIndex = graph.getIndex(startVertex)
  # test depth first search
  print ("Depth First Search from", startVertex)
  graph.dfs (startIndex)
  print()

  # test breadth first search
  print ("Breadth First Search from", startVertex)
  graph.bfs (startIndex)
  print()

  output = []
  copy=graph.getAdjMat()
  if (not graph.hasCycle(copy)):
    # test topological sort
    print ("Topological Sort")
    output = graph.toposort()
  else:
    # test minimum cost spanning tree
    print("Minimum Cost Spanning Tree from", startVertex)
    output = graph.spanTree(startIndex)
    
  for e in output:
    print(e)
  print()

  # test single source shortest path algorithm
  print("Shortest Path from",startVertex)
  graph.shortestPath(startVertex)
  
main()
