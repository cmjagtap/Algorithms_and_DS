def findDuplicates(array):
	if not array:
		return None
	else:
		array.sort()
		for x in xrange(0,len(array)-1):
			if array[x]==array[x+1]:
				print "duplicate",array[x]
array=[1,2,3,4,2,3,4,]
findDuplicates(array)