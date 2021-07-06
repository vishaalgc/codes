"""
https://leetcode.com/problems/maximum-product-subarray/submissions/
https://leetcode.com/problems/maximum-product-subarray/discuss/847520/Thought-process-and-useful-strategy
"""


# DYNAMIC PROGRAMMING

class Solution:

    def maxProduct(self,nums):

        curMax,curMin = nums[0],nums[0]
        ans = curMax

        for i in range(1,len(nums)):
            temp = curMax
            curMax = max(temp*nums[i],nums[i],curMin*nums[i])
            curMin = min(temp*nums[i],nums[i],curMin*nums[i])
            ans = max(ans,curMax)

        return ans
