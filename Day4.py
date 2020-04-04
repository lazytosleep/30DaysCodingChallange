# Prob: Move zeros to the end without using extra space in o(n) complexity
# Move zeros to end inplace following two pointer approach
# This is 0(n2), lets try out better way of doing it


def moveZerosToEndInplace(nums):
    for i in range(0, len(nums)):
        nonZeroIdx = i
        while nums[nonZeroIdx] == 0:
            if nonZeroIdx == len(nums) - 1:
                break
            nonZeroIdx = nonZeroIdx + 1
        nums[i], nums[nonZeroIdx] = nums[nonZeroIdx], nums[i]
    return nums


'''
So we will use the fact that elements are either zero or non zero
if we can move all zeros to the front and track the position 
where non zero is ending, we can simply change remaining to zero
'''


def moveZerosToEndBetterWay(nums):
    left, right = 0, 0
    while right < len(nums):
        if nums[right] != 0:
            nums[left] = nums[right]
            left += 1
        right += 1

    while left < len(nums):
        nums[left] = 0
        left += 1
    return nums


print(moveZerosToEndBetterWay([0, 1, 0, 3, 6]))
