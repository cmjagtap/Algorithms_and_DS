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
			self.data.remove(self.data[0])
q=queue()
q._dequeue()
q._enqueue(1)
q._enqueue(2)
q._enqueue(3)
q._enqueue(4)
print "Q is ",q.data[:]
print "_front_:- ",q._front_()
print "_rear_:- ",q._rear_()
q._dequeue()
q._enqueue(44)
print "_front_:- ",q._front_()
print "_rear_:- ",q._rear_()
print "Q is ",q.data[:]
