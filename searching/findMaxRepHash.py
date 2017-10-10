def maxFreq(array):
	if not array:
		return None
	else:
		max=0
		hash_table={}
		for x in array:
			if x in hash_table:
				hash_table[x]+=1
			elif x!=' ':
				hash_table[x]=1
			else:
				hash_table[x]=0
		for x in array:
			if hash_table[x]>max:
				max=hash_table[x]
				maxRepEle=x
		print maxRepEle,"repeted",max,"times"

array=[1,2,3,4,1,2,2,1,2,2,2,2,3]
maxFreq(array)
