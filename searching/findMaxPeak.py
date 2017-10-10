def maxPeak(array):
	if not array:
		return None
	else:
		peak=array[0]
		for x in xrange(1,len(array)-2):
			prev=array[x-1]
			cur=array[x]
			next=array[x+1]
			if cur>prev and cur>next:
				if peak<cur:
					peak=cur

		if array[len(array)-1]>array[len(array)-2]:
			cur=array[len(array)-1]
			if peak<cur:
				peak=cur
		return peak

A = [35, 5, 80, 2, 40, 25, 80, 25, 15, 70]
print A, "\n", maxPeak(A)