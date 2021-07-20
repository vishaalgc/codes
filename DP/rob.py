class Solution:
    def rob(self, nums) -> int:
        n = len(nums)
        dp = list(nums)
        
        for i in range(n):
            j = i+2
            for j in range(i+2,n,1):
                if j < n:
                    dp[j] = max(dp[j],nums[j]+dp[i])
        return max(dp)
                    
            
        
s = Solution()
nums = [2,7,9,3,1]
# nums = [1,2,3,1]
# nums = [2,1,1,2]
print(s.rob(nums))