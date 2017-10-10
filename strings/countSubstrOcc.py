def countSubsrt(string,substr):
	if not string or substr:
		return
	else:
		count=0
		for x in range(len(string)-len(substr)+1):
			if string[x:x+len(substr)]==substr:
				count+=1
		return count
print countSubsrt("ABCDCDC","CDC")