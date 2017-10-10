class double_ended_queue():

	def __init__(self):
		self.data = []
	def is_empty(self):
		if len(self.data)==0:
			return True
	def d_first_(self):
		if len(self.data)==0:
			return -1
		else:
			return self.data[0]
	def d_last(self):
		if len(self.data)==0:
			return -1
		else:
			return self.data[-1]
	def d_add_first(self,element):
		return self.data.insert(0,element)
	def d_add_last(self,element):
		return self.data.append(element)
	def d_del_first(self):
		if len(self.data)==0:
			print "Can't _dequeue queue is_empty"
		else:
			self.data.remove(self.data[0])
	def d_del_last(self):
		if len(self.data)==0:
			print "Can't _dequeue queue is_empty"
		else:
			self.data.remove(self.data[-1])
	def display_q(self):
		print self.data[:]

q=double_ended_queue()
print q.d_first_()
print q.d_last()
q.d_add_last(2) 
q.d_add_last(3)
q.d_add_last(4)
q.d_add_first(5)
q.d_add_first(1)
print q.d_first_()
print q.d_last()
print "display_q",q.display_q()
