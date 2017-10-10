class Vertex:
	def __init__(self, node):
		self.id = node
	def getVertexID(self):
		return self.id
	def setVertexID(self,id):
		self.id=id

class Graph:
	def __init__(self,noOfVertices,cost=0):
		self.adjMatrix=[[-1]*noOfVertices for _ in range(noOfVertices)]
		self.noOfVertices = noOfVertices
		self.vertices=[]
		for i in range(0,noOfVertices):
			newVertex=Vertex(i)
			self.vertices.append(newVertex)
	
	def setVertex(self,vxt,id):
		if 0<=vxt<self.noOfVertices:
			self.vertices[vxt].setVertexID(id)

	def getVertex(self,n):
		for vertx in range(0,self.noOfVertices):
			if n==self.vertices[vertx].getVertexID():
				return vertx
		else:
			return -1
	def addEdge(self,frm,to,cost=0):
		if self.getVertex(frm)!=-1 and self.getVertex(to)!=-1:
			self.adjMatrix[self.getVertex(frm)][self.getVertex(to)]=cost 
			#two way connection undirected graph if graph directed do'nt add below line
			self.adjMatrix[self.getVertex(to)][self.getVertex(frm)]=cost
	

	def getEdges(self):
		edges=[]
		for v in range(0,self.noOfVertices):
			for u in range(0,self.noOfVertices):
				if self.adjMatrix[u][v]!=-1:
					vid=self.vertices[v].getVertexID()#from vertex
					wid=self.vertices[u].getVertexID()#to vertex
					edges.append((vid,wid,self.adjMatrix[u][v]))#adjmat for cost of edge
		return edges
	
	def printAdjancy(self):
		for v in range(0,self.noOfVertices):
			row=[]
			for u in range(0,self.noOfVertices):
				row.append(self.adjMatrix[v][u])
			print row

G=Graph(5)#5 nodes graph
G.setVertex(0,'a')
G.setVertex(1,'b')
G.setVertex(2,'c')
G.setVertex(3,'d')
G.setVertex(4,'e')

G.addEdge('a','b',10)
G.addEdge('a','c',20)
G.addEdge('b','d',15)
G.addEdge('d','e',10)
G.addEdge('e','c',5)

print 'Adjanct matrix is'
G.printAdjancy()
print G.getEdges()