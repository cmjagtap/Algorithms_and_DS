def findDuplicates(array):
	if not array:
		return None
	else:
		for x in xrange(0,len(array)):
			for y in xrange(x+1,len(array)):
				if array[x]==array[y]:
					print "duplicate",array[x]
								
array=[1,2,3,4,2,3,4,]
findDuplicates(array)