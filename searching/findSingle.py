def findSingleNO(array):
	if not array:
		return None
	else:
		res=0
		for x in xrange(0,len(array)):
			res=res^array[x]
		return res

array=[1,2,1,2,3]
print findSingleNO(array)