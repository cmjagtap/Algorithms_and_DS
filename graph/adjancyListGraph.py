class Vertex:
	def __init__(self, node):
		self.id =node
		self.adjacent={}
	def getVerID(self):
		return self.id
	def addNeighbour(self,neighbour,cost=1):
		self.adjacent[neighbour]=cost
	def getConnections(self):
		return self.adjacent.keys()
	def getWt(self,neighbour):
		return self.adjacent[neighbour]

class Graph:
	def __init__(self):
		self.vertexDict = {}
		self.numOfVer=0
	def __iter__(self):
		return iter(self.vertexDict.values())

	def setVertex(self,n):
		self.numOfVer+=1
		newVer=Vertex(n)
		self.vertexDict[n]=newVer
		return newVer
	
	def getVertex(self,n):
		if n in self.vertexDict:
			return self.vertexDict[n]
		else:
			return None
	
	def addEdges(self,frm,to,cost=1):
		if frm in self.vertexDict and to in self.vertexDict:
			self.vertexDict[frm].addNeighbour(self.vertexDict[to],cost)
			self.vertexDict[to].addNeighbour(self.vertexDict[frm],cost)
	
	def getEdges(self):
		edges=[]
		for v in G:
			for u in v.getConnections():
				vid=v.getVerID()
				wid=u.getVerID()
				edges.append((vid,wid,v.getWt(u)))
		return edges


G=Graph()
G.setVertex('a')
G.setVertex('b')
G.setVertex('c')
G.addEdges('a','b',11)
print "graph data"
print G.getEdges()