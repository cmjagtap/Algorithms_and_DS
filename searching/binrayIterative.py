def binaryItrative(array,key):
	if not array:
		return None
	high=len(array)-1
	low=0
	while low<=high:
		mid=(low+high)/2
		if array[mid]<key:	low=mid+1
		elif array[mid]>key: high=mid-1
		else:
			return mid
	return -1

array=[1,2,3,4,5,5,6,7,8]
print binaryItrative(array,22)
