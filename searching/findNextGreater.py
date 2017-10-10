def nextGreater(array):
	if not array:
		return None
	else:
		nextGreater=array[0]
		for x in xrange(0,len(array)-1):
			for y in xrange(x+1,len(array)):
				if array[x]<array[y]:
					nextGreater=array[y]
					break
			print "next greater for",array[x],"is",nextGreater

array=[1,4,2,3,5]
nextGreater(array)