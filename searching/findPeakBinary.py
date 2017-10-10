def findPeak(array):
	if not array:
		return None
	low=0
	high=len(array)-1
	while low+1<high:
		mid=(low+high)/2
		if array[mid]<array[mid-1]:
			high=mid
		elif array[mid]>array[mid+1]:
			low=mid
		else:
			return mid
array = [35, 5, 20, 2, 40, 25, 80, 25, 15, 40]
print findPeak(array)
