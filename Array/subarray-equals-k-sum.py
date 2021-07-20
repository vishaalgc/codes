"""
https://leetcode.com/problems/subarray-sum-equals-k/
"""

import bisect
class Solution:
    def subarraySum(self, nums, k: int) -> int:
       # as there can be negative values, we need to use prefix sum concept
    
        prefixSum = []
        n = len(nums)
        i = 0
        sm = 0
        ans = 0
        for i in range(n):
            bisect.insort(prefixSum,sm)
            sm += nums[i]
            # check if sm - someXPrefixSum == k
            if sm == k:
                ans+=1
            x = bisect.bisect_left(prefixSum,sm-k)
            print(i,x,prefixSum,sm)
            if x < n and x > 0:
                if sm-k == nums[x]:
                    ans+=1
            
        return ans

s = Solution()
nums = [1,1,1]
k = 2
nums = [1,2,3]
k = 3

nums = [1,2,1,2,1]
k = 3
print(s.subarraySum(nums,k))

                    
            
            
            
            
        
            
            
            
        