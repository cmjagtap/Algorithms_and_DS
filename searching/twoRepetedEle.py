def twoRepEle(array):
	if not array:
		return None
	else:
		hash_table={}
		for x in array:
			if x in hash_table:
				hash_table[x]+=1
			elif x !=' ':
				hash_table[x]=1
			else:
				hash_table[x]=0
		for x in array:
			if hash_table[x]==2:
				print x
array=[1,2,3,1,2,5,6,7]
twoRepEle(array)