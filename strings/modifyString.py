#Task: Read a given string, change the character at a given index and then print the modified string.
def modifystr(string,pos,char):
	if not string or pos<1:
		return None
	else:
		temp=list(string)
		temp.insert(pos,char)
		return "".join(temp)
string="abracadabra"
print modifystr(string,5,"k")
