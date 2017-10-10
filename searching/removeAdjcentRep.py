def removRepted(array):
	if not array:
		return None
	else:
		i=1
		while i<len(array):
			if array[i]==array[i-1]:
				array.pop(i)
				i-=1
			i+=1
		array=''.join(array)
		return array
string="mississipi"
print removRepted(list(string))