def bubbleSort(array):
	if not array:
		return None
	else:
		for x in range(len(array)):
			for y in range(x+1,len(array)):
				if array[x]>array[y]:
					temp=array[x]
					array[x]=array[y]
					array[y]=temp
def swap(array,x,y):
	temp=array[x]
	array[x]=array[y]
	array[y]=temp
array=[7,6,5,4,3,2,1]
bubbleSort(array)
print array