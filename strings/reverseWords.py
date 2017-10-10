def reverse(word):
	string=list(word)
	lenght=len(word)-1
	i=0
	while i<lenght:
		string[i],string[lenght]=string[lenght],string[i]
		i+=1
		lenght-=1
	return "".join(string)

def reverseWords(string):
	if not string:
		return None
	else:
		string=string.split()
		temp=[]
		i=0
		while i<len(string):
			temp.append(reverse(string[i]))
			i+=1
		return " ".join(temp)
string="hello i am cm"
print "before string",string
print "revese of words",reverseWords(string)