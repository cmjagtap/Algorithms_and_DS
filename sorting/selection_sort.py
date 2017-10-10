def selectionSort(array):
	if not array:
		return None
	else:
		for x in range(len(array)):
			minNo=x
			for y in range(x+1,len(array)):
				if array[y]< array[minNo]:
					minNo=y
			swap(array,minNo,x)
def swap(array,a,b):
	temp=array[a]
	array[a]=array[b]
	array[b]=temp
array=[1,2,3,7,5,4,3,2,1]
selectionSort(array)
print array
