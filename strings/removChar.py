def removeChar(string,char):
	if not string:
		return None
	else:
		temp=[]
		for x in range(0,len(string)):
			if string[x]!=char:
				temp.append(string[x])
		return "".join(temp)
print "removed char",removeChar("hello","l")
