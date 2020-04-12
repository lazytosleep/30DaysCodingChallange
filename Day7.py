'''
In in array count the number of elements passing arr[j] = arr[i] +1 where  0<i,j<len(array) 
'''
def countPlusOnes(arr):
    mySet = set()
    for ele in arr:
        mySet.add(ele)
    result = 0
    for ele in arr:
        if(mySet.__contains__(ele + 1)):
            result +=1
    return result


print(countPlusOnes([1, 1, 2, 2]))

