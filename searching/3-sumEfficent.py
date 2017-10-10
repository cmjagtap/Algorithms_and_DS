def threeSum(array,k):
	if not array:
		return None
	else:
		lenght=len(array)
		for x in xrange(0,lenght-2):
			left=x+1
			right=lenght-1
			while left<right:
				if array[x]+array[left]+array[right]==k:
					print array[x],array[left],array[right]
					return
				elif array[x]+ array[left]+array[right]<k:
					left+=1
				else:
					right-=1
		return None
array=[2,1,5,4,3]
array.sort()
threeSum(array,6)


def replaceWithNearestGreaterElement(A):
	nextNearestGreater = float("-inf")
	i = j = 0
	for i in range(0, len(A) - 1):
		nextNearestGreater = float("-inf")
		for j in range(i + 1, len(A)):
			if A[i] < A[j]:
				nextNearestGreater = A[j]
				break
		print("For the element " + str(A[i]) + ", " + str(nextNearestGreater) + " is the nearest greater element")

replaceWithNearestGreaterElement([6, 2, 4, 1, 2, 1, 2, 2, 10])