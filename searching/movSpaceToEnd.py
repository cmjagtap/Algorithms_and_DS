def moveSpace(string):
	if not string:
		return None
	else:
		count=0
		datalist=list(string)
		for x in xrange(0,len(string)):
			if not datalist[x].isspace():
				datalist[count]=datalist[x]
				count+=1
		while count<len(string):
			datalist[count]=' '
			count+=1
		string=''.join(datalist)
	return string

string="move spacce to End"
print moveSpace(string)