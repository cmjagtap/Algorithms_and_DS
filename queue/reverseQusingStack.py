class queue():

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
			x=self.data[0]
			self.data.remove(self.data[0])
		return x

class Array_Stack():
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

q=queue()
s=Array_Stack()
q._enqueue(1)
q._enqueue(2)
q._enqueue(3)

print "Before reverse Q is",q.data
while not q.is_empty():
	s._push_(q._dequeue())

while not s.is_empty():
	q._enqueue(s._pop_())

print "After reverse Q is",q.data