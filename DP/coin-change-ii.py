class Solution:
    def minNumberOfWays(self,coins,targetAmount):
        
        dp = [0]*(targetAmount+1)
        dp[1] = 1
        
        for i in range(1,targetAmount+1):
            for coin in coins:
                if coin >= i and i+coin <= targetAmount:
                    dp[i+coin] = dp[i+coin]+dp[i]
            print(dp)
        return dp[targetAmount]


s = Solution()
A = [1,2,5]
B = 5
print(s.minNumberOfWays(A,B))