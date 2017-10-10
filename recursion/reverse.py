#Reverse using recursion
def Reverse(data,start,stop):
	if start<stop-1:
		data[start],data[stop-1]=data[stop-1],data[start]
		Reverse(data,start+1,stop-1)
data=range(1,10)
print data
Reverse(data,0,len(data))
print data