def checkPairSorted(array):
	if not array:
		return None
	else:
		for x in xrange(0,len(array)-1,2):
			if array[x]>array[x+1]:
				return False
		return True
array = [34, 48, 10, 13, 2, 80, 30, 23]
print checkPairSorted(array)
array = [34, 48, 10, 13, 2, 80, 20, 23]
print checkPairSorted(array)