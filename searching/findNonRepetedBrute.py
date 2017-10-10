def findNonRepeated(array):
	if not array:
		return None
	else:
		for x in xrange(0,len(array)):
			nonRep=0
			for y in xrange(0,len(array)):
				if x!=y and array[x]==array[y]:
					nonRep=1
			if nonRep==0:
				return array[x]

array=[1,1,1,2,2,2,3,4,5,6]
print findNonRepeated(array)