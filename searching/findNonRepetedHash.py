def findNonRepeat(string):
	if not string:
		return None
	else:
		hash_table={}
		for char in string:
			if char in hash_table:
				hash_table[char]+=1
			elif char !=' ':
				hash_table[char]=1
			else:
				hash_table[char]=0
		for char in string:
			if hash_table[char]==1:
				print("the first non repeated character is: %s" % (char))
				return char

		return

print findNonRepeat("aaabbcdsx")