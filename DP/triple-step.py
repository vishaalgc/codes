class Solution:
    def stairs(self,n):

        dp = [0]*(n+1)
        dp[0] = 1
        steps = [1,2,3]
        for i in range(n+1):
            for step in steps:
                if i+step <= n:
                    dp[i+step] = dp[i+step]+dp[i]
        return dp[n]

s = Solution()
y = s.stairs(5)
print(y)
