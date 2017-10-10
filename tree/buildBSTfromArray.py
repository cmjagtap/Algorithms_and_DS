#build a BST from a sorted Array
class bstNode:
	def __init__(self,data=None):
		self.data = data
		self.left=None
		self.right=None
		

def buildBSTfromArray(array,left,right):
	if(left>right):
		return None
	newnode=bstNode()
	if not newnode:
		print "Mem error node not created"
		return
	if left==right: # if only one element in array
		newnode.data=array[left]
	else:
		mid=left+(right-left)/2
		newnode.data=array[mid]
		newnode.left=buildBSTfromArray(array,left,mid-1)
		newnode.right=buildBSTfromArray(array,mid+1,right)
	return newnode


def sortedArrayToBST(root, array):
	length = len(array)
	if length == 0: 
		return None
	if length == 1: 
		return bstNode(array[0])
	root = bstNode(array[length / 2])
	root.left = sortedArrayToBST(root,array[:length / 2])
	root.right = sortedArrayToBST(root,array[length / 2 + 1:])
	return root

def printBst(root):
	if not root:
		return
	else:
		printBst(root.left)
		print root.data
		printBst(root.right)
def preorder(root):
	if not root:
		return None
	else:
		print root.data
		preorder(root.left)
		preorder(root.right)

Array=[1,2,3,4,5,6]
root=buildBSTfromArray(Array,0,len(Array)-1)
print "inorder"
printBst(root)
print "preorder"
preorder(root)
arr=[1,2,3,4,5,6]
root1=None
sortedArrayToBST(root1,arr)
print "Inorder"
printBst(root)
print "preorder"
preorder(root)


