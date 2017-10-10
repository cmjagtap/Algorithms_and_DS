def insertionSort(array):
	if not array:
		return None
	else:
		for i in range(1,len(array)):
			tmp=array[i]
			k=i
			while k>0 and tmp<array[k-1]:
				array[k]=array[k-1]
				k-=1
			array[k]=tmp
array=[1,2,3,7,5,4,3,2,1]
insertionSort(array)
print(array)
