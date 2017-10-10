class stack:
	def __init__(self):
		self.data= []
	def is_empty(self):
	    return not self.data
	def _push_(self,ele):
		self.data.append(ele)
	def _pop_(self):
		return self.data.pop()

def isPalindrom(string):
	ispal=False
	s=stack()
	for char in string:
		s._push_(char)
		
	if len(string)<1:
		return False
	else:
		for char in string:
			if char == s._pop_():
				palindrome = True
			else:
				palindrome = False
		return palindrome

print isPalindrom("madam")
print isPalindrom("zabc")