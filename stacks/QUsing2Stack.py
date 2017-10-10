class Stack():
	def __init__(self):
		self.data=[]
	def _len_(self):
		return len(self.data)
	def is_empty(self):
		if len(self.data)==0:
			return True
	def _top_(self):
		if len(self.data)==0:
			print ('Stack is uderflow')
		else:
			return self.data[-1]
	def _push_(self,elemnt):
		self. data.append(elemnt)
	
	def _pop_(self):
		if self.is_empty():
			print "Stack is uderflow"
		else:
			return self.data.pop()
class Queue:
	def __init__(self):
		self.stk1=Stack()
		self.stk2=Stack()
	def is_empty(self):
		if self.stk1.is_empty() and self.stk2.is_empty():
			return True
	
	def enqueue(self,elemnt):
		self.stk1._push_(elemnt)
	
	def dequeue(self):
		if not self.stk2.is_empty():
			return self.stk2._pop_()
		else:
			while not self.stk1.is_empty():
				self.stk2._push_(self.stk1._pop_())
			return self.stk2._pop_()
				




q=Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print q.dequeue()
print q.dequeue()
print q.dequeue()