'''
Maxmize profit by buying and selling multiple times
'''
class Solution:
    # brute force approach just works
    def maximizeProfit(self, arr, start) -> int:
        maxSoFor = 0
        if start == len(arr):
            return maxSoFor
        for i in range(start, len(arr)-1):
            for j in range(i+1, len(arr)):
                if arr[j] > arr[i]:
                    max = arr[j] - arr[i] + self.maximizeProfit(arr, j+1)
                    if max > maxSoFor:
                        maxSoFor = max
        return maxSoFor


print(Solution().maximizeProfit([7,1,5,3,6,4], 0))

