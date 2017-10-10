def removeAdDup(string):
	if not string:
		return None
	else:
		temp=[]
		for x in range(0,len(string)):
			if string[x]!=string[x-1]:
				temp.append(string[x])
		return temp
string="1234212222233"
print "After removed",removeAdDup(string)

