def maxRep(array):
	if not array:
		return None
	else:
		conter=maxcounter=1
		index=array[0]
		for x in xrange(0,len(array)):
			conter=0
			for y in xrange(0,len(array)):
				if x!=y and array[x]==array[y]:
					conter+=1
			if maxcounter<conter:
				maxcounter=conter
				index=x
		return array[index],maxcounter
array=[1,2,3,4,54,56,6,1,1,2,2,3,3,3,3]
print "Element, max No of occurances",maxRep(array)