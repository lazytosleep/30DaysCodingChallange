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

