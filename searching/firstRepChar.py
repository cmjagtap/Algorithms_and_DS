def firstRepchar(string):
	if not string:
		return None
	else:
		hash_table={}
		for char in string:
			if char in hash_table:
				hash_table[char]+=1
				print "first rep char ", char
				return
			elif char!=' ':
				hash_table[char]=1
			else:
				hash_table[char]=0

firstRepchar('abxb')