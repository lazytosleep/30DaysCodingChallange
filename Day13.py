def contiguousSubArray(nums)-> int:
    myDict = dict()
    sum = 0
    maxSoFor = 0
    for i in range(0, len(nums)):
        val = nums[i]
        if val == 0:
            val = -1
        sum += val
        if sum == 0:
            maxSoFor = max(i + 1, maxSoFor)
        if myDict.get(sum) == None:
            myDict[sum] = i
        else:
            diff = i - myDict[sum]
            maxSoFor = max(maxSoFor, diff)
    return maxSoFor


print(contiguousSubArray([0, 1, 0, 1]))
