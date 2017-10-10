class LinkedStack:
	#Node declaration	
	class Node:
		def __init__(self,element,next):
			self.element= element
			self.next = next
	#Stacks methods
	def __init__(self):
		self._head =None
		self._size=0
	def _len_(self):
		return self._size
	def is_empty(self):
		return self._size==0
	def _top_(self):
		if self._size==0:
			print "empty Stack"
		else:
			return self._head.element
	def _push_(self,element):
		self._head=self.Node(element,self._head)
		self._size+=1
	def _pop_(self):
		if self._size==0:
			print "empty Stack"
		else:
			x = self._head.element
			self._head = self._head.next
			self._size -=1
		return x
	def printStack(self):
		if self.is_empty():
			print "Stack is underflow"
		else:
			current=self._head
			while current!=None:
				print current.element
				current=current.next
s=LinkedStack()
s._push_(1)
s._push_(2)
s._push_(3)
print "top is ",s._top_()
s.printStack()
s._pop_()
print "top is ",s._top_()
print "Lenth of stack is ",s._len_()
s.printStack()
