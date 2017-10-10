
#Binary Search
def binary_search(data,low,high,key):
	if low>high:
		return False
	else:
		mid=((low+high)/2)
		if key==data[mid]:
			return True
		elif key<data[mid]:
			return binary_search(data,low,mid-1,key)
		else:
			return binary_search(data,mid+1,high,key)
print "Searh no",binary_search(range(1,10),0,9,5)