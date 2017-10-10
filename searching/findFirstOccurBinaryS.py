def findBinarySearch(array,key):
	if not array:
		return None
	high=len(array)-1
	low=0
	mid=0
	last=-1
	while 1:
		if low>high:
			return last
		mid=(low+high)/2
		if array[mid]==key:
			last=mid;high=mid-1
		if array[mid]<key:
			low=mid+1
		if array[mid]>key:
			high=mid-1
	return mid

A = [5, 6, 9, 12, 15, 21, 21, 34, 45, 57, 70, 84]
print findBinarySearch(A,21)