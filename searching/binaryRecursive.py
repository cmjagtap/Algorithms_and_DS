def binaryRec(array,low,high,key):
	if not array:
		return -1
	if low==high:
		if array[low]==key:
			return low
		else:
			return -1
	mid=(low+high)/2
	if array[mid]<key:
			return binaryRec(array,mid+1,high,key)
	elif array[mid]>key:
			return binaryRec(array,low,mid,key)
	else:
		return mid

array=[1,2,3,4,5,6,7,8]
print binaryRec(array,0,len(array)-1,99)