class binaryTree:
	def __init__(self,data):
		self.data=data #root
		self.left=None
		self.right=None
	def setData(self,data):
		self.data=data
	def getData(self):
		return self.data
	def setLeft(self,left):
		self.left=left
	def getLeft(self):
		return self.left
	def setRight(self,right):
		self.right=right
	def getRight(self):
		return self.right
	def insertLeft(self,node):
		if self.left==None:
			self.left=binaryTree(node)
		else:
			temp=binaryTree(node)
			temp.left=self.left
			self.left=temp
	def insertRight(self,node):
		if self.right==None:
			self.right=binaryTree(node)
		else:
			temp=binaryTree(node)
			temp.right=self.right
			self.right=temp
def inorder(root):
	if root==None:
		return None
	else:
		inorder(root.getLeft())
		print root.getData()
		inorder(root.getRight())
def preorder(root):
	if root==None:
		return None
	else:
		print root.getData()
		preorder(root.getLeft())
		preorder(root.getRight())
def postorder(root):
	if root==None:
		return None
	else:
		postorder(root.getLeft())
		postorder(root.getRight())
		print root.getData()

def isBst(root):
	if not root:
		return True
	if root.left and root.data<root.left.data:
		return False
	if root.right and root.data>root.right.data:
		return False
	if not isBst(root.left) or not isBst(root.right):
		return False
	return True

root=binaryTree(1)
root.insertLeft(2)
root.insertRight(3)
root.insertLeft(4)
root.insertRight(5)
print root.getData()
print "Inorder traversal"
inorder(root)
print "preorder traversal"
preorder(root)
print "postorder traversal"
postorder(root)
print isBst(root)