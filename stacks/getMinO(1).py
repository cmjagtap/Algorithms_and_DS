class getMinStack():
	def __init__(self):
		self.data=[]
		self.min=[]
	def _len_(self):
		return len(self.data)
	def is_empty(self):
		return (self.data)==0
	def _top_(self):
		if len(self.data)==0:
			print ('Stack is uderflow')
		else:
			return self.data[-1]
	def _push_(self,elemnt):
		self. data.append(elemnt)
		if not self.min or elemnt<=self.Stack_min():
			self.min.append(elemnt)

	def _pop_(self):
		if (self.data)==0:
			print "Stack is uderflow"
		else:
			x=self.data.pop()
			if x==self.Stack_min():
				self.min.pop()
			return x
	def Stack_min(self):
		return self.min[-1]
	def display_stack(self):
		if len(self.data)==0:
			return "Stack underflow"
		else:
			return self.data[::-1]

obj=getMinStack()
print "Display ",obj.display_stack()

obj._push_(6)
obj._push_(5)
obj._push_(4)
obj._push_(3)
obj._push_(2)
obj._push_(1)
print "Top of Stack",obj._top_()
print "Stack_min",obj.Stack_min()
print "Pop elemnt ",obj._pop_()
print "Top of Stack",obj._top_()
print "Display ",obj.display_stack()
print "Top of Stack",obj._top_()
print "Pop elemnt ",obj._pop_()
print "Top of Stack",obj._top_()
print "Stack_min",obj.Stack_min()
print "Display ",obj.display_stack()
