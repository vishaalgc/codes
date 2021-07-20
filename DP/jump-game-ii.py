class Solution:
    def jump(self, nums):
        
        n = len(nums)
        dp = [2**31]*n
        dp[0] = 0
        
        for i in range(n):
            end = nums[i]+i
            for j in range(end,i,-1):
                if j < n:
                    if dp[j] > dp[i]+1:
                        dp[j] = dp[i]+1
                    else:
                        break
                    
                    print(i,j,dp)
            
        # print(dp)
        return dp[n-1]
        
s = Solution()
nums = [2,3,1,1,4]
# nums = [2,3,0,1,4]
# nums = [1]
# nums = [2,1]

nums = [1,2,3]
print(s.jump(nums))