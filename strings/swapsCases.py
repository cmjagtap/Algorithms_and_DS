def swapCase(string):
	if not string:
		return None
	else:
		temp=[]
		for char in string:
			if char.isupper():
				temp.append(char.lower())
			elif char.islower():
				temp.append(char.upper())
			elif char ==" ":
				temp.append(char)
			else:
				temp.append(char)

		return "".join(temp)
string="HackerRank.com presents Pythonist 2"
print " switch",swapCase(string)
