class stackA:
	def __init__(self):
		self.data= []
	def is_empty(self):
	    return not self.data
	def _push_(self,ele):
		self.data.append(ele)
	def _pop_(self):
		return self.data.pop()

def reverse(stack):
	def reverseRec(stack,newstk=stackA()):
		if not stack.is_empty():
			newstk._push_(stack._pop_())
			reverseRec(stack,newstk)
		return newstk
	return reverseRec(stack)
			
			
s=stackA()
s._push_(1)
s._push_(2)
s._push_(3)
s._push_(4)
print "Display stack",s.data[::-1]
s=reverse(s)
print "after reverse stack",s.data[::-1]