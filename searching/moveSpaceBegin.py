def moveSpaceBeg(string):
	if not string:
		return None
	else:
		datalist=list(string) #we convert string to list
		count=length=len(string)-1
		for x in xrange(length,-1,-1):
			if not datalist[x].isspace():
				datalist[count]=datalist[x]
				count-=1
		while count>=0:
			datalist[count]=' '
			count-=1
		string=''.join(datalist)
	return string
string="move spacce to infront"
print moveSpaceBeg(string)
