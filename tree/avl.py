class avlNode:
	def __init__(self,data,balFactor,left,right):
		self.data =data
		self.balFactor=balFactor
		self.left=left
		self.right=right
class avlTree:
 	def __init__(self):
 		self.root = None
 	def insertAvl(self,data):
 		newnode=avlNode(data,0,None,None)
 		