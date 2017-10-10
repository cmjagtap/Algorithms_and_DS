#find two maximum nos
def findMaxtwo(data):
        i=0;j=len(data)-1
        if(len(data)<=1):
                return None,None
        else:
                max1=data[0]
                max2=data[j]
                while i<len(data):
                        if data[i]>max1 and data[i]!=max2:
                                max1=data[i]
                        elif data[j]>max2 and data[j]!=max1:
                                max2=data[j]
                        i+=1
                        j-=1
                return max1,max2
data=[11,2,3,4,9,3,5,6]
print "findMaxtw",findMaxtwo(data)

#print duplicates
def findDuplicates(data):
        if len(data)<=1:
           return None
        else:
            temp=[]
            for x in data:
                if data.count(x)>1:
                    temp.append(x)
            return set(temp)
data=[1,2,3,3,4,4,5,6,6]
print "Array ",data
print "Duplicates",findDuplicates(data)

#split Array into two half
def splitArray(data):
        array1=[];mid=0
        array2=[]
        if len(data)<=1:
                return None
        else:
                mid=(len(data))/2
                for x in xrange(0,mid):
                    array1.append(data[x])
                for x in range(mid,len(data)):
                    array2.append(data[x])
                return array1,array2
print "Array before split",data
print "Two Arrays are:- ",splitArray(data)





def pythonMergeSort(theList):
    if len(theList) <= 1 :
        return theList
    else :
        mid = (len(theList)/ 2)
        leftHalf = pythonMergeSort( theList[ :mid ])
        rightHalf = pythonMergeSort( theList[ mid: ])
        newList = mergeOrderedLists( leftHalf, rightHalf )
        return newList
data=[11,2,3,5,1,9,0]
# print "Merge sort ",pythonMergeSort(data)

#rotate array left by k
def rotateLeftArray(data,k):
    if len(data)<=1 or k<1:
        return None
    else:
        temp=[];i=0
        for x in range(0,k):
            temp.append(data[x])
        for x in range(k,len(data)):
            data[i]=data[x]
            i+=1
        for x in xrange(0,k):
            data[x+i]=temp[x]
        return data
print "Array before rotate left",data
print "Array after rotate",rotateLeftArray(data,3)

def reverseArray(data):
    return data[::-1]
print "Array",data
print "reverseArray",reverseArray(data)

#find majority element x appears more than n/2 times in
def  majorityEle(data):
    length=len(data)
    if length<1:
        return None
    elif length==1:
        return data[0]
    else:
        for x in data:
            if data.count(x)>(length/2):
                return x
data=[3,2,1,1,1]
print "majority element",majorityEle(data)

# Given an unsorted array of numbers, write a function that returns true 
# if array consists of consecutive numbers.
# Examples:
# a) If array is {5, 2, 3, 1, 4}, then the function should return true
#  because the array has consecutive numbers from 1 to 5.
def cosucativeArray(data):
    flag=0
    if len(data)<1 :
        return False
    elif len(data)==1:
        return True
    else:
        if (max(data)-min(data))+1==len(data):
            return True
        for x in data: 
            data.count(x) not >1:
        
data=[1,2,3,4]
print "Is cosucativeArray",cosucativeArray(data)
