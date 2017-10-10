def findPeak(array):
	if not array:
		return None
	else:
		for i in xrange(1,len(array)-2):
			prev=array[i-1]
			cur=array[i]
			next=array[i+1]
			if cur>prev and cur>next:
				print cur
		if array[len(array)-1]>array[len(array)-2]:
			print array[len(array)-1]

array = [35, 5, 20, 2, 40, 25, 80, 25, 15, 40]
print array, "\n"
findPeak(array)