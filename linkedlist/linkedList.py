#Author cm
#if found bug mail me cmjagtap1@gmail.com
#function List implimented as follows
# 1) create node and init linkedList
# 2) addNode, addNodefirst,addNodeLast
# 3) printList
# 4) lenghtList
# 5) getFirst
# 6) getLast
# 7) searchKey
# 8) additionofList
# 9) oddEvenPositionSum
# 10) delList,delLast,delfirst
# 11) delElementByPos
# 12) getEleementBypos
# 13) getMiddle
# 14) getNodeValueFromTail
# 15) removeElement
# 16) findLoop
# 17) ReverseList
# 18) Reverse in pairs
# 19) split into two lists
# 20) Merge two lists
# 21) is even terminated

class Node:
	def __init__(self,data):
		self.data = data
		self.next=None
	def setData(self,data):
		self.data=data
	def getData(self):
		return self.data
	def setNext(self,next):
		self.next = next
	def getNext(self):
		return self.next
	def hasNext(self):
	 	return self.next!=None

class linkedList:
	def __init__(self):
		self.head = None
		self.lenght=0
	def addNode(self,node):
		if self.lenght==0:
			self.addNodeBeg(node)
		else:
			self.addNodeLast(node)
	
	def addNodeBeg(self,node):
		newnode=node
		newnode.next=self.head
		self.head = newnode
		self.lenght+=1

	def addNodeLast(self,node):
		newnode=node
		newnode.next=None
		current=self.head
		while current.next!=None:
			current=current.next
		current.next=newnode
		self.lenght+=1

	def printList(self):
		current=self.head
		while current!=None:
			print current.data
			current=current.next
	def printListGiven(self,head):
		current=head
		while current!=None:
			print current.data
			current=current.next

	def lenghtList(self):
		return self.lenght

	def getFirst(self):
		if self.lenght<1:
			return "Empty List"
		else:
			return self.head.data
	
	def getLast(self):
		if self.lenght<1:
			return "Empty List"
		else:
			current=self.head
			while current.next!=None:
				current=current.next
			return current.data
	
	def searchKey(self,key):
		if self.lenght<1:
			return "Cant searchKey Empty List"
		else:
			current=self.head
			while current!=None:
				if current.data==key:
					return True
				current=current.next
			return False
	def additionList(self):
		if self.lenght<1:
			return None
		else:
			current=self.head
			sumlist=0
			while current!=None:
				sumlist+=current.data
				current=current.next
			return sumlist
	#function return even position sum and odd position sum
	def oddEvenPosSum(self):
		if self.lenght<=1:
			return None
		else:
			flag="odd";sumodd=0;sumeven=0
			current=self.head
			while current!=None:
				if flag=="odd":
					sumodd+=current.data
					flag="even"
				elif flag=="even":
					sumeven+=current.data
					flag="odd"
				current=current.next
			return sumodd,sumeven
	
	#python has garbage collector
	def delList(self):
		self.head=None
		self.lenght=0
	
	def delLast(self):
		if self.lenght==0: #empty list
			return None
		elif self.lenght==1: #only one node that del
			 self.head=None
			 self.lenght-=1
		else:
			current=self.head;prev=None
			while current.next!=None:
				prev=current
				current=current.next
			prev.setNext(None)
			self.lenght-=1
	def delByPos(self,pos):
		if self.lenght<1 or pos>self.lenght or pos<0:
			print "Invalid position"
		else:
			if pos==1:
				self.head=self.head.next
			elif pos==self.lenght:
				self.delLast()
			else:
				i=1;
				current=self.head
				prev=None
				while i<pos and current!=None:
					prev=current
					current=current.next
					i+=1
				prev.next=current.next
				self.lenght-=1
	def getEleBypos(self,pos):
		if self.lenght<1 or pos>self.lenght or pos<0:
			print "Invalid position"
		else:
			if pos==1:
				return self.head.data
			else:
				i=1;
				current=self.head
				while i<pos and current!=None:
					current=current.next
					i+=1
				return pos,current.data
	def getMiddle(self):
		fastptr= self.head
		slowptr=self.head;i=0
		if fastptr==None or fastptr.next==None:
			return None
		else:
			while fastptr.next!=None:
				if i==0:
					fastptr=fastptr.next
					i=1
				elif i==1:
					slowptr=slowptr.next
					fastptr=fastptr.next
					i=0
			return slowptr.data
	
	def getNodeValueFromTail(self,positionTail):
		current=self.head;value=0;i=0
		count_=self.lenght
		value=count_- positionTail
		if current==None or positionTail<1 or value<1:
			return None
		else:
			while i!=value:
				current=current.next
				i+=1
			return current.data
	
	def removeEle(self,key):
		if self.head==None:
			return "Element not in list"
		else:
			curNode=self.head
			prevNode=None;
			while curNode is not None and curNode.data != key:
				prevNode=curNode
				curNode=curNode.next
			prevNode.next=curNode.next

	def findLoop(self):
		fastptr=self.head;slowptr=self.head
		if fastptr==None:
			return False
		else:
			while fastptr!=None and slowptr!=None and fastptr.next!=None:
					slowptr=slowptr.next
					fastptr=fastptr.next.next
					if fastptr==slowptr:
						return True

	def reverseList(self):
		last = None
		current = self.head
		while(current is not None):
			nextNode = current.next
			current.next=last 
			last = current
			current = nextNode
		self.head = last 
	def reverseinPair(self):
		current=self.head
		if current==None or current.next==None:
			return None
		else:
			x=None
			while current!=None and current.next!=None :
				self.swapNode(current,current.next)
				current=current.next.next
	
	def swapNode(self,a,b):
		tmp=a.getData()
		a.setData(b.getData())
		b.setData(tmp)
	
	def splitList(self):
		if self.head==None or self.head.next==None:
			return None
		else:
			fast =self.head
			slow = self.head
			while fast and fast.next:
				s=slow
				slow = slow.getNext()
				fast = fast.getNext()
				fast = fast.getNext()
				middle=slow
			s.setNext(None)
			return self.head, middle
	
	def mergeList(self,list1,list2):
		temp=list1
		if list1==None:
			return list2
		elif list2==None:
			return list1
		else:
			while list1.next:
				list1=list1.next
			list1.next=list2
			return temp
	
	def isListEvenLenght(self):
		current = self.head
		while current!= None and current.next!= None:
			current = current.next.next
		if current == None:
			return True
		return False
	def rotateList(self,k):
		if self.head==None or k<0:
			return None
		else:
			i=0
			current=self.head;
			temp2=self.head
			temp=None
			while current!=None and i<k:
				i+=1
				current=current.next
			self.head.setNext(current)
			temp=current
			current.setNext(None)
			while temp.next!=None:
				temp=temp.next
			temp.setNext(temp2)


ll=linkedList()
ll.addNode(Node(1))
ll.addNode(Node(2))
ll.addNode(Node(3))
ll.addNode(Node(5))
ll.addNode(Node(6))
ll.addNodeBeg(Node(4))
ll.printList()
print "lenght of list",ll.lenghtList()
print "getFirst",ll.getFirst()
print "getLast",ll.getLast()
print "search T/F",ll.searchKey(3)
print "additionList",ll.additionList()
print "Sum of odd position and even position is ",ll.oddEvenPosSum()
#print "Del List",ll.delList()
ll.delLast() #del last
print "List\n",
ll.printList()
ll.addNodeLast(Node(6))
ll.delByPos(3)
print "after del delByPos"
ll.printList()
print "Get getEleBypos",ll.getEleBypos(2)
print "getMiddle",ll.getMiddle()
print "getNodeValueFromTail",ll.getNodeValueFromTail(2)
print "findLoop",ll.findLoop()
print "removeEle",ll.removeEle(3)
ll.reverseList()
ll.printList()
print "reverseinPair",ll.reverseinPair()
ll.printList()
x,y=ll.splitList()
print "List 1 is"
ll.printListGiven(x)
print "List 2 is"
ll.printListGiven(y)
z=ll.mergeList(x,y)
print "After merge"
ll.printListGiven(z)
print "isListEvenLenght T/F",ll.isListEvenLenght()

#print "rotateList"
#ll.rotateList(1)
ll.printList()
