class Solution:
    def minPossibleCoins(self,coins,targetAmount):

        dp = [targetAmount+1]*(targetAmount+1)
        dp[0] = 0
        
        for i in range(targetAmount+1):
            for coin in coins:
                if i+coin <= targetAmount:
                    dp[i+coin] = min(dp[i+coin],dp[i]+1)
        return dp[targetAmount]

s = Solution()
A = [1,2,5]
B = 11
print(s.minPossibleCoins(A,B))

        

