def findDuplicatesHash(array):
	if not array:
		return None
	else:
		hash_table={}
		for x in range(0,len(array)):
			if x in hash_table:
				hash_table[x]+=1
			elif x!=' ':
				hash_table[x]=1
			else:
				hash_table[x]=0
		for x in array:
			if hash_table[x]>1:
				print "duplicate",hash_table[x]

array=[1,1,1,2,3,1,2,4,5]
findDuplicatesHash(array)