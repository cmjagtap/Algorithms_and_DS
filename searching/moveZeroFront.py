def moveZeroFront(array):
	if not array:
		return None
	else:
		counter=lenght=len(array)-1
		for x in xrange(lenght,-1,-1):
			if array[x]!=0:
				array[counter]=array[x]
				counter-=1
		while counter>=0:
			array[counter]=0
			counter-=1
		return array
array=[1,2,0,4,5,0,6,0]
print moveZeroFront(array)