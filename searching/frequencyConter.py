def frequency(array):
	if not array:
		return None
	else:
		hash_table={}
		for x in array:
			if x in hash_table:
				hash_table[x]+=1
			elif x!=' ':
				hash_table[x]=1
			else:
				hash_table[x]=0
		for x in array:
			print x,"---->",hash_table[x]

array=[1,2,1,1,2,3,3,4,5,6,7]
frequency(array)


