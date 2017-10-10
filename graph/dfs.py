class Vertex:
	def __init__(self,id):
		self.id= id
		self.adjacent={}
		self.visited=False
	def setVID(self,id):
		self.id=id
	def getVID(self):
		return self.id
	def getConnections(self):
		return self.adjacent.keys()
	def addNeighbour(self,neighbour,cost):
		self.adjacent[neighbour]=cost
	def getWt(self,node):
		return self.adjacent[node]
	def setVisited(self):
		self.visited=True
class Graph:
	def __init__(self):
		self.noOfVertices = 0
		self.vertexDict={}
	def __iter__(self):
		return iter(self.vertexDict.values())

	def addVertex(self,node):
		self.noOfVertices+=1
		newvert=Vertex(node)
		self.vertexDict[node]=newvert
		return newvert
	def getVertex(self,node):
		if node in self.vertexDict:
			return self.vertexDict[node]
		else:
			return None
	def addEdge(self,frm,to,cost):
		if frm in self.vertexDict and to in self.vertexDict:
			self.vertexDict[frm].addNeighbour(self.vertexDict[to],cost)
	def getEdges(self):
		edges=[]
		for v in G:
			for u in v.getConnections():
				vid=v.getVID()
				wid=u.getVID()
				edges.append((vid,wid,v.getWt(u)))
		return edges


def DFSTravrse(G,v):
	v.setVisited()
	print "travrsal",v.getVID()
	for nbr in v.getConnections():
		if nbr.visited==False:
			nbr.setVisited()
			DFSTravrse(G,nbr)

def DFS(G):
	for v in G:
		if v.visited==False:
			DFSTravrse(G,v)



G=Graph()
G.addVertex('a')
G.addVertex('b')
G.addVertex('c')
G.addVertex('d')
G.addVertex('e')
G.addVertex('f')
G.addEdge('a', 'b', 1)  
G.addEdge('a', 'c', 1)
G.addEdge('b', 'd', 1)
G.addEdge('b', 'e', 1)
G.addEdge('c', 'd', 1)
G.addEdge('c', 'e', 1)
G.addEdge('d', 'e', 1)
G.addEdge('e', 'a', 1)
print 'Graph data:'
print G.getEdges()
DFS(G)