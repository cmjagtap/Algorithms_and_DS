#Author cm
#if found bug mail me cmjagtap1@gmail.com
#function List implimented as follows
#1) create insert init bst
#2) inorder,preorder,postorder
#3) 
class bstNode:
	def __init__(self, data):
		self.data =data
		self.left=None
		self.right=None

def insertBst(root,ele):
	newnode=bstNode(ele)
	if not root:
		root=newnode
	else:
		if root.data>newnode.data:
			if not root.left:
				root.left=newnode
			else:
				insertBst(root.left,ele)
		else:
			if not root.right:
				root.right=newnode
			else:
				insertBst(root.right,ele)
def inorder(root):
	if not root:
		return None
	else:
		inorder(root.left)
		print root.data
		inorder(root.right)
def preorder(root):
	if not root:
		return None
	else:
		print root.data
		preorder(root.left)
		preorder(root.right)
def postorder(root):
	if not root:
		return None
	else:
		postorder(root.left)
		postorder(root.right)
		print root.data
def countNodes(root):
	if not root:
		return 0
	else:
		return (countNodes(root.left)+1+(countNodes(root.right)))

def SumofBst(root):
	if not root:
		return 0
	else:
		return root.data+SumofBst(root.left)+SumofBst(root.right)
def findMaxRec(root):
	if not root:
		return None
	elif root.right==None:
		return root.data
	else:
		return findMax(root.right)
def findMax(root):
	if not root:
		return None
	else:
		while root.right!=None:
			root=root.right
		return root.data
def findMin(root):
	if not root:
		return None
	else:
		while root.left!=None:
			root=root.left
		return root.data

def depthorHeight(root):
	leftHeight=0
	rightHeight=0
	if not root:
		return 0
	else:
		leftHeight=depthorHeight(root.left)
		rightHeight=depthorHeight(root.right)
		if leftHeight>rightHeight:
			return leftHeight+1
		else:
			return rightHeight+1
def search(root,key):
	if not root:
		return None
	elif root.data==key:
		return True
	else:
		return search(root.left,key) or search(root.right,key)
def convertIntoMirror(root):
	temp=None
	if not root:
		return None
	else:
		convertIntoMirror(root.left)
		convertIntoMirror(root.right)
		temp=root.left
		root.left=root.right
		root.right=temp


def areMirror(tree1,tree2):
	if not tree1 and not tree2:
		return True
	elif not tree1 or not tree2:
		return False
	elif tree1.data != tree2.data:
		return False
	else:
		return areMirror(tree1.left,tree2.right) and areMirror(tree1.right,tree2.left)

def areStructSame(tree1,tree2):
	if not tree1 and not tree2:
		return True
	elif not tree1 or not tree2:
		return False
	else:
		return  areStructSame(tree1.left,tree2.left) and areStructSame(tree1.right,tree2.right)
#full nodes means which left and right not none
def printFullNodes(root):
	if not root:
		return None
	else:
		printFullNodes(root.left)
		if root.left!=None and root.right!=None:
			print root.data
		printFullNodes(root.right)
def printLeafNode(root):
	if not root:
		return None
	else:
		printLeafNode(root.left)
		if root.left==None and root.right==None:
			print root.data
		printLeafNode(root.right)
def printAncestor(root):
	if not root:
		return None
	else:
		printAncestor(root.left)
		if not root.left or not root.right:
			print root.data
		printAncestor(root.right)


def CountOfTreesFromNodes(noOFnodes):
	if noOFnodes<=1:
		return 1
	else:
		totalTrees=0
		for root in range(1,noOFnodes+1):
			leftTrees=CountOfTreesFromNodes(root-1)
			rightTrees=CountOfTreesFromNodes(noOFnodes - root)
			# number of possible trees with this root == left*right
			totalTrees +=leftTrees*rightTrees
		return totalTrees

def rangeNodes(root,fromK,toK):
	if not root:
		return None
	else:
		rangeNodes(root.left,fromK,toK)
		if root.data>=fromK and root.data<=toK:
			print root.data
		rangeNodes(root.right,fromK,toK)

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

root=bstNode(1)
insertBst(root,3)
insertBst(root,5)
insertBst(root,4)
print "preorder"
preorder(root)
print "inorder"
inorder(root)
print "postorder"
postorder(root)
print "Count of nodes is",countNodes(root)
print "depthorHeight",depthorHeight(root)
print "SumofBst",SumofBst(root)
print "findMax",findMax(root)
print "findMaxRec",findMaxRec(root)
print "findMin",findMin(root)
print "search T/F",search(root,3)
root_x=bstNode(1)
insertBst(root_x,3)
insertBst(root_x,5)
insertBst(root_x,4)
convertIntoMirror(root_x)
print "areMirror ",areMirror(root,root_x)
root2=bstNode(6)
insertBst(root2,7)
insertBst(root2,9)
insertBst(root2,8)
print "are structurally same",areStructSame(root,root2)
insertBst(root,6)
print "Full node is"
printFullNodes(root)
print "LeafNodes"
printLeafNode(root)
print "printAncestor"
printAncestor(root)
print "CountOfTreesFromNodes",CountOfTreesFromNodes(3)
print "Nodes between from k to k"
rangeNodes(root,2,5)
print isBst(root) #for non bst we need to construct non bst
