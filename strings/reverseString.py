def reverseStrings(string):
	if not string:
		return None
	else:
		lenght=len(string)-1
		i=0
		while i<lenght:
			string[i],string[lenght]=string[lenght],string[i]
			i+=1
			lenght-=1
		return "".join(string)
print "reverse of string is:-",reverseStrings(list("hello"))