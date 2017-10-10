#Recursive palindrome
def isPalindrom(data):
	if len(data)<=1:
		return True
	else:
		return data[0] == data[-1] and isPalindrom(data[1:-1])
data='heh'
print isPalindrom(data)
