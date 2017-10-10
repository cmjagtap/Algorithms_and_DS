def moveZeroEnd(array):
	if not array:
		return None
	else:
		length=len(array)
		count=0
		for x in xrange(0,length):
			if array[x]!=0:
				array[count]=array[x]
				count+=1
		while count<length:
			array[count]=0
			count+=1
		return array
array=[1,0,0,2,3,0,4,5,6]
print moveZeroEnd(array)