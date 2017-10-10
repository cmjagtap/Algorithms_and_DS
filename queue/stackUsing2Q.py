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
class stackUQ:
	def __init__(self):
		self.q1=queue()
		self.q2=queue()
	
	def is_empty(self):
		return self.q1.is_empty() and self.q2.is_empty()
	
	def _push_(self,ele):
		if self.q2.is_empty():
			self.q1._enqueue(ele)
		else:
			self.q2._enqueue(ele)
	
	def _pop_(self):
		if self.is_empty():
			print "stack underflow cant pop"
		elif self.q2.is_empty():
			while not self.q1.is_empty():
				cur=self.q1._dequeue()
				if self.q1.is_empty():
					return cur
				self.q2._enqueue(cur)
		else:
			while not self.q2.is_empty():
				cur=self.q2._dequeue()
				if self.q2.is_empty():
					return cur
				self.q1._enqueue(cur)
s=stackUQ()
s._push_(1)
s._push_(2)
s._push_(3)
print s._pop_()
print s._pop_()
print s._pop_()