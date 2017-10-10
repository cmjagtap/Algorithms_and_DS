def findMajority(array):
	if not array:
		return None
	else:
		count=0
		element=-1
		for x in xrange(0,len(array)-1):
			if count==0:
				element=array[x]
				count+=1
			elif element==array[x]:
				count+=1
			else:
				count-=1
		return element
array=[1,2,3,4,3,3,3,5,26,3]
print findMajority(array)

