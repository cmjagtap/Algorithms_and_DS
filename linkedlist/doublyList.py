#Author cm
#if found a bug mail me cmjagtap1@gmail.com
#function List implimented as follows
# 1) create,init doubly linked list
# 2) insert ,insertFirst,insertLast
# 3) find element

class Node:
	def __init__(self,data,next,prev):
		self.data = data
		self.next = next
		self.prev = prev
	def setData(self,data):
		self.data=data
	def getData(self):
		return self.data
	def setNext(self,next):
		self.next=next
	def getNext(self):
		return self.next!=None
	def setPrev(self,prev):
		self.prev=prev
	def getPrev(self):
		return self.prev!=None
class doubly:
	def __init__(self):
		self.head = None
		self.tail = None
	
	def insert(self,data):
		if self.head==None:
			self.head=Node(data,None,None)
			self.tail=self.head
		else:
			current=self.head
			while current.next!=None:
				current=current.next
			current.next=Node(data,None,current)
			self.tail=current.next
	
	def printList(self):
		if self.head==None:
				print "empty List"
		else:
			current=self.head
			while current!=None:
				print current.data
				current=current.next
	
	def printReverse(self):
		if self.head==None:
			print "empty List"
		else:
			current=self.tail
			while current!=None:
				print current.data
				current=current.prev

	def insertFirst(self,data):
		newnode=Node(data,None,None)
		if self.head==None:
			self.head=newnode
			self.tail=self.head
		else:
			newnode.setPrev(None)
			newnode.setNext(self.head)
			self.head.setPrev(newnode)
			self.head=newnode
	def insertLast(self,data):
		newnode=Node(data,None,None)
		if self.head==None:
			self.head=newnode
			self.tail=self.head
		else:
			current=self.head
			while current.next !=None:
				current=current.next
			newnode.setPrev(current)
			current.setNext(newnode)
	
	def findEle(self,key):
		if self.head==None:
			return False
		else:
			current=self.head
			while current!=None:
				if current.data==key:
					return True
				current=current.next
			return False


dl=doubly()
dl.insert(1)
dl.insert(2)
dl.insertFirst(0)
dl.insertFirst(-1)
dl.insertLast(3)
dl.insertLast(4)
dl.insertLast(5)
dl.printList()
print "Reverse using prev"
dl.printReverse()
print "findEle T/F", dl.findEle(1)
print "findEle T/F", dl.findEle(21)
