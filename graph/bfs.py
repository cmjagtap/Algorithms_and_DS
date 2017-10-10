import sys
class Queue():

	def __init__(self):
		self.data = []
	def is_empty(self):
		if len(self.data)==0:
			return True
	def _front_(self):
		if len(self.data)==0:
			return -1
		else:
			return self.data[0]
	def _rear_(self):
		if len(self.data)==0:
			return -1
		else:
			return self.data[-1]
	def _enqueue(self,element):
		return self.data.append(element)
	def _dequeue(self):
		if len(self.data)==0:
			print "Can't _dequeue queue is_empty"
		else:
			self.data.remove(self.data[0])
	def size(self):
		return len(self.data)

class Vertex:
	def __init__(self,node):
		self.id = node
		self.adjancy={}
		self.visited=False
		self.distance=sys.maxint
		self.prev=None
	def setVid(self,id):
		self.id=id
	def getVid(self):
		return self.id
	def addNeighbour(self,neighbour,cost=0):
		self.adjancy[neighbour]=cost
	def getConnection(self):
		return self.adjancy.keys()
	def getWt(self,node):
		return self.adjancy[node]
	def setVisited(self):
		self.visited=True
	def setDistance(self,dist):
		self.distance=dist
	def setPrev(self,prev):
		self.prev=prev
	def getDistance(self):
		return self.distance
	def __str__(self):
		return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjancy])

class Graph:
	def __init__(self):
		self.vertexDict = {}
		self.noOfVertices=0
	def __iter__(self):
		return iter(self.vertexDict.values())

	def addVertex(self,node):
		self.noOfVertices+=1
		newVertx=Vertex(node)
		self.vertexDict[node]=newVertx
		return newVertx
	
	def getVertex(self,node):
		if node in self.vertexDict:
			return self.vertexDict[node]
		else:
			return None
	def addEdge(self,frm,to,cost):
		if frm in self.vertexDict and to in self.vertexDict:
			self.vertexDict[frm].addNeighbour(self.vertexDict[to],cost)

	def getEdges(self):
		egdes=[]
		for v in G:
			for u in v.getConnection():
				vid=v.getVid()
				wid=u.getVid()
				egdes.append((vid,wid,v.getWt(u)))
		return egdes

def BfsTravrsal(G,s,q):
	q._enqueue(s.getVid())
	while q.size>0:
		curvert=G.getVertex(q._dequeue())
		print curvert
		for neighbour in curvert.getConnection():
			if neighbour.visited==False:
				neighbour.setVisited()
				q._enqueue(neighbour)



def BFS(G):
	q=Queue()
	for v in G:
		if v.visited==False:
			BfsTravrsal(G,v,q)

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
#print G.getEdges()
BFS(G)