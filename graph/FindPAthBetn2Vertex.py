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


def CountOfVertex(G):
	if not G:
		return None
	else:
		count=0
		for v in G:
			count+=1
		return count

def CountVertes(G):
	return G.noOfVertices

def CountOfEdges(G):
	return G.noOfEdges

def pathBetweenTwoVertex(G,source,dest,path=[]):
	if not G:
		return None
	else:
		path=path.append(source)
		if source==dest:
			return path
		if source not in G:
			return []
		for v in G:
			if v not in path:
				extendedPath=pathBetweenTwoVertex(v,dest,path)
				for p in extendedPath:
					path.append(p)
		return path


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
print "count of veterx is",CountOfVertex(G)
print "count of vertex using inbuilt",CountVertes(G)
print "count of edges",CountOfEdges(G)
print "pathh between two vertex",pathBetweenTwoVertex(G,'a','b')
