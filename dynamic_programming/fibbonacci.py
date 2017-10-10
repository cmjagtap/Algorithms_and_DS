def fibbo(t1,t2,no):
	fib=[t1,t2]
	for i in range(2,no+1):
		fib.append(fib[i-1]+fib[i-2])
	print fib[no]
t1,t2,no=map(int,raw_input().split())
fibbo(t1,t2,no)


# def fibbo(no):
# 	fib=[0,1]
# 	for i in range(2,no+1):
# 		fib.append(fib[i-1]+fib[i-2])
# 	return fib[no]
# print "fib no",fibbo(3)
