'''
Max subarray: Given an array fine the contigious sub-array with max sum 
'''
def maxIncludingMidArray(arr, low, mid, high) -> int:
    sum_ = 0
    # tracks max sum found so far
    left = -9999999
    for i in range(mid, low - 1, -1):
        sum_ = sum_ + arr[i]
        if sum_ > left:
            left = sum_
    # tracks max sum found so far
    right = -99999999
    sum_ =0
    for i in range(mid + 1, high + 1):
        sum_ = sum_ + arr[i]
        if sum_ > right:
            right = sum_
    return left + right

'''
We can have only three situation here
Max in left hand side which is same as original problem so we can simply recurse
Max in right hand side which is again same as original problem so simply recurse
Or Max is crossing mid element, in this case get the max by trversing left and right hand side and adding them

e.g. if we have three element then its either left or right or left + mid or left + mid + right or mid + right
What is time complexity for this 0(nlogn) why? prove it.
'''

def maxSumSubArrayInner(arr, low, high) -> int:
    if low == high:
        return arr[low]
    mid = (low + high) // 2

    # assuming left subarray is maximum
    left = maxSumSubArrayInner(arr, low, mid)

    # assuming right sub array is maximum
    right = maxSumSubArrayInner(arr, mid + 1, high)

    # assuming max includes mid element
    includingMid = maxIncludingMidArray(arr, low, mid, high)

    return max(left, right, includingMid)


class Solution:
    # Maximum Subarray
    def maxSubArray(self, nums) -> int:
        return maxSumSubArrayInner(nums, 0, len(nums)-1)


print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))