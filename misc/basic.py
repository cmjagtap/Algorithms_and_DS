
animals=['Cat','Dog','lion','tiger']
eats=['mouse','dog food','deer','deer']
for i in animals:
	print i

lis=[]
for x in animals:
	for y in x:
		lis.append(y)
print lis

def square(n):
	return n*n

def sum_of_digit(n):
	sumdigit=0
	for x in str(n):
		sumdigit+=int(x)
	return sumdigit

def no_is_palindrom(n):
	no=str(n)
	j=0
	i=len(no)-1
	flag=0
	while i>0:
		if(no[i]!=no[j]):
			flag=1
		i-=i
	if flag==1:
		return 0
	else:
		return 1


def Armstrong_no(n):
	no=str(n)
	arms=0
	for x in no:
		s=int(x)
		arms+=(s*s*s)
	if n==arms:
		return 1
	else:
		return 0

#very famous problem given heads and legs find no of pigs and chiken
def find_no_of_pigs_and_chiken(numHeads,numLegs): 
	for numchiks in range(0,numHeads+1):
		numpigs=numHeads-numchiks
		totalLegs=4*numpigs+2*numchiks
		if totalLegs==numLegs:
			return[numpigs,numchiks]
	return[None,None]

print "Square of given no is ", square(12)
print "sum of digit is ", sum_of_digit(123)
print "no_is_palindrom T/F",no_is_palindrom(121)
pigs,chiken=find_no_of_pigs_and_chiken(20,56)
print "pigs and chiken ",pigs,chiken
