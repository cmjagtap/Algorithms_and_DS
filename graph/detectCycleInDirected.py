class stack:
	def __init__(self):
		self.data = []
	def _push_(self,ele):
		self.data.append(ele)
	def _pop_(self):
		return self.data.pop()
	def isEmpty(self):
		return len(self.data)==0

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
		self.noOfEdges=0
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
			self.noOfEdges+=1
			self.vertexDict[frm].addNeighbour(self.vertexDict[to],cost)
	
	def getEdges(self):
		edges=[]
		for v in G:
			for u in v.getConnections():
				vid=v.getVID()
				wid=u.getVID()
				edges.append((vid,wid,v.getWt(u)))
		return edges

def CountVertes(G):
	return G.noOfVertices
def CountOfEdges(G):
	return G.noOfEdges

def Detecting(G,v,s):
	v.setVisited()
	for nbr in v.getConnections():
		if nbr.visited==False:
			nbr.setVisited()
			s.append(nbr.getVID())
			Detecting(G,nbr,s)
		else:
			if nbr.getVID() in s:
				return True
	s.append(v.getVID())
	return False
def detectCycleinDirected(G):
	if not G:
		return None
	else:
		s=[]
		t=False
		for v in G:
			if v.visited==False:
				t=Detecting(G,v,s)
		if t==True:
			print "Cycle found"
		elif t==False:
			"graph not contain cycle"


G=Graph()
G.addVertex('a')
G.addVertex('b')
G.addVertex('c')
G.addVertex('d')
G.addVertex('e')
G.addVertex('f')
G.addVertex('g')
G.addVertex('h')
G.addVertex('i')
G.addVertex('j')
G.addEdge('a', 'b', 1)  
G.addEdge('b', 'c', 1)
G.addEdge('b', 'h', 1)
G.addEdge('d', 'e', 1)
G.addEdge('d', 'c', 1)
G.addEdge('d', 'i', 1)
G.addEdge('d', 'h', 1)
G.addEdge('e', 'i', 1)
G.addEdge('g', 'a', 1)
G.addEdge('g', 'b', 1)
G.addEdge('g', 'c', 1)
G.addEdge('i', 'c', 1)
G.addEdge('j', 'e', 1)
print 'Graph data:'
print G.getEdges()
print "count of vertex using inbuilt",CountVertes(G)
print "count of edges",CountOfEdges(G)
detectCycleinDirected(G)