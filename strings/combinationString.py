def combinations(string):
	if not string:
		return None
	else:
		level=['']
		for i in range(len(string)):
			nList = []
			for item in level:
				nList.append(item + string[i])
				level += nList
		return level[1:]

print "combinations of ", combinations("abc")

			