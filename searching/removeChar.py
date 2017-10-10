def removeChar(string,char):
	if not string:
		return None
	else:
		temp=list(string)
		i=0
		while i<len(temp):
			if temp[i]==char:
				temp.remove(char)
				i=i-1
			i=i+1
		string=''.join(temp)
		return string
string="hello"
print removeChar(string,"e")

