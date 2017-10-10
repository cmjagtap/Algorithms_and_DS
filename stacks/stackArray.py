class Array_Stack():
	def __init__(self):
		self.data=[]
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
	def _pop_(self):
		if (self.data)==0:
			print "Stack is uderflow"
		else:
			return self.data.pop()
	def display_stack(self):
		if len(self.data)==0:
			return "Stack underflow"
		else:
			return self.data[::-1]

obj=Array_Stack()
print "Display ",obj.display_stack()

obj._push_(1)
obj._push_(2)
obj._push_(3)
obj._push_(4)
obj._push_(5)
obj._push_(6)
print "Top of Stack",obj._top_()
print "Pop elemnt ",obj._pop_()
print "Top of Stack",obj._top_()
print "Display ",obj.display_stack()
print "Top of Stack",obj._top_()
print "Pop elemnt ",obj._pop_()
print "Top of Stack",obj._top_()
print "Display ",obj.display_stack()

