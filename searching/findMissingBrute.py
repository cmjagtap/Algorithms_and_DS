def findMissing(array):
	if not array:
		return None
	else:
		for x in xrange(1,len(array)+1):
			found=0
			for y in xrange(0,len(array)):
				if array[y]==x:
					found=1
			if found==0:
				print "Missig no",x

A = [8, 2, 1, 4, 6, 5,  9]
findMissing(A)