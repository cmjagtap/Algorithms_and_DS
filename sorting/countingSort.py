def countingSort(array, maxval):
    n = len(array)
    m = maxval + 1
    Countarr = [0] * m #count array with 0 init
    for ele in array: #updating count of element
        Countarr[ele] += 1           
    
    index = 0
    for ele in range(m):            
        for c in range(Countarr[ele]): 
            array[index] = ele #each count of element in output array
            index += 1
    return array

array=[1,4,4,3,2,9]
print countingSort(array,10)

