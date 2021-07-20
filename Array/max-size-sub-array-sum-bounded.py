"""
https://leetcode.com/problems/minimum-size-subarray-sum/
https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/
    2 3 1 2 4 3
    0 2 5 6 8 12 15

    1 4 4
    0 1 5 9
"""


import bisect
class Solution:

    def getLeftGreat(self,prefixSums,x):
        lt = []
        rt = []
        for i in range(len(prefixSums)):
            while lt and prefixSums[i] >= lt[-1]:
                lt.pop()
            if lt:
                rt = lt[-1]
            else:
                rt.append(None)
            lt.append(prefixSums[i])
        return rt
                 

    def shortestSubarray(self, nums, k) -> int:
        sm = 0
        prefixSums = []
        minLen = 2**31-1
        for i in range(len(nums)):
            prefixSums.append(sm)

        
        if minLen == 2**31-1:
            minLen = -1
        return minLen

s = Solution()
target = 7
# nums = [2,3,1,2,4,3]
# nums = [1,4,4]
# target = 4
# target = 11
# nums = [1,1,1,1,1,1,1,1]
nums = [2,-1,2]
k = 3
# nums = [48,99,37,4,-31]
# k = 140
print(s.shortestSubarray(nums,k))