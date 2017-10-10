class Linked_Q:
	class Node:
		__slots__='element','next'

		def __init__(self,element,next):
			self.element = element
			self.next=next			
	def __init__(self, ):
		self._head = None
		self._tail=None
		self._size=0
	def len(self):
		return self._size
	def is_empty(self):
		return self._size==0
	def _front_(self):
		return self._head.element
	def _rear_(self):
		return self._tail.element
	def _dequeue_(self):
		if self._size==0:
			print "Queue is_empty"
		else:
			x=self._head.element
			self._head=self._head.next
			self._size -=1
			if self._size==0:
				self._tail=None
			return x
	def _enqueue_(self,element):
		newnode = self.Node(element, None)
		if self._size==0:
			self._head=newnode
		else:
			self._tail.next = newnode
		self._tail=newnode
		self._size +=1
        def printQ(self):
                temp=self._head
                if temp==None:
                        return "Empty Q"
                else:
                        while temp!=None:
                                print temp.element
                                temp=temp.next
                        
                        
        
q=Linked_Q()
q._enqueue_(1)
q._enqueue_(2)
q._enqueue_(3)
print "_front_",q._front_()
print "_rear_",q._rear_()
print "Q contains"
q.printQ()
q._dequeue_()
print "_front_",q._front_()
print "_rear_",q._rear_()
print "Q contains"
q.printQ()
