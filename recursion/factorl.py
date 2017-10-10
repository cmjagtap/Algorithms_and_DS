#factorial of no
def factorial(no):
	if no==0:
		return 1;
	else:
		return no*factorial(no-1)
print "factorial of 5 is",factorial(5)