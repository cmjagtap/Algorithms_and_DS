def mergeSort(array):
	if not array:
		return None
	if len(array)>1:
		mid=len(array)/2
		lefthalf=array[:mid]
		righthalf=array[mid:]
		mergeSort(lefthalf)
		mergeSort(righthalf)
		i=j=k=0
		while i<len(lefthalf) and j<len(righthalf):
			if lefthalf[i]<righthalf[j]:
				array[k]=lefthalf[i]
				i+=1
			else:
				array[k]=righthalf[j]
				j+=1
			k+=1
		while i<len(lefthalf):
			array[k]=lefthalf[i]
			i+=1
			k+=1
		while j<len(righthalf):
			array[k]=righthalf[j]
			j+=1
			k+=1
array=[1,2,3,7,5,4,3,2,1]
mergeSort(array)
print(array)