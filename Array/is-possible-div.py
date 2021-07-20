"""
https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/
"""

class Solution:
    def isPossibleDivide(self, nums, k: int) -> bool:
        if k > len(nums):
            return False
        mp = {}
        for num in nums:
            mp[num] = mp.get(num,0)+1
        lt = sorted(set(nums))
        
        for key in lt:
            freq = mp[key]
            if freq > 0:
                for j in range(0,k):
                    if key + j not in mp or mp[key+j] < freq:
                        return False
                    mp[key+j] -= freq
        return True

s = Solution()
nums = [3,2,1,2,3,4,3,4,5,9,10,11]
k = 3
print(s.isPossibleDivide(nums,k))
        
        
        
            
        
        
            
        
        