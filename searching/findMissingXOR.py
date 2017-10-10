def findMissing(array):
	if not array:
		return None
	else:
		x=0
		lenghtr=len(array)
		for i in range(1,lenghtr+2):
			x = x ^ i
		for y in range(0,lenghtr):
			x = x ^ array[y]
		print "missing no is",x

A = [8, 2, 1, 4, 6, 5, 7, 9]
findMissing(A) 
