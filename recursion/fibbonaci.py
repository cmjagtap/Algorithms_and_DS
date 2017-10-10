#fibbonaci
def fibonnaci(n):
	if n==0 or n==1:
		return 1;
	else:
		return fibonnaci(n-1)+fibonnaci(n-2)
print "fibonnaci no 5 is ",fibonnaci(5)