#define a function is n is multiple of m
def is_multiple(n,m):
	if n%m == 0: return True
	else: return False

print "Check is is_multiple:-",is_multiple(4,2)

#define function which returns tuple of two no maximum and minimum
def mini_max(List1):
	if len(List1)<1: return None,None
	else:
		max_no=List1[0]
		min_no=List1[0]
		for x in List1:
			if(max_no<x): max_no=x
			else:
				if min_no>x: min_no=x
		return max_no,min_no

List1=[1,2,3,5,4,-2,-4,8]
print "Maximum is and Minimum no is:-",mini_max(List1)

#print list like 8, 6, 4, 2, 0, -2, -4, -6, -8
print range(8,-10,-2)

#genate power set List
List2=[2**x for x in range(1,10)]
print List2

#genrate List of Square 
print [x*x for x in xrange(1,10)]


# Print even nos
print [x for x in xrange(11,20) if x%2==0]

#print divisible by 3 and 7 nos between 1-50
print [x for x in xrange(1,50) if x%3==0 and x%7==0]

#print duplicates
list3 = [1,2,3,4,4,5,5,6,1]
print set([x for x in list3 if list3.count(x) > 1])
print set([x for x in list3 if list3.count(x) > 1])

#genrate the list [0, 2, 6, 12, 20, 30, 42, 56, 72, 90]
list3=range(1,11)
print [x*(x-1) for x in list3]

#print ['a','b'...'z']
print [chr(x) for x in xrange(97,123)]

#count no_of vowels
def countVowels(string):
	count=0
	for ch in string:
		if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u':
			count+=1
	return count
print countVowels('aeiou')


def is_even(no):
	if not isinstance(no,(int,float)): 
		raise TypeError("no must be numeric")
	elif no<0:
		raise TypeError("No shuld be positive")
	else:
		if no%2==0: return True
		else: return False
print "Is no even:-",is_even(11)
print "Is no even:-",is_even(2)

def testException():
	try:
		fp = open( 'ex.txt' )
	except IOError as e:
		print(" Exception: ", e)
testException()
