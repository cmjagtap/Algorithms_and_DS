def factorial(no):
	fact=[1]
	if no==0:
		return fact[0]
	else:
		for x in xrange(1,no+1):
			fact.append(x*fact[x-1])
		return fact[no]
print "factorial",factorial(120)