"""
Maximum path sum in matrix
https://www.geeksforgeeks.org/coin-change-dp-7/
"""

class Solution:

    def printer(self,lt):
        for i in range(len(lt)):
            x = ''
            for j in range(len(lt[i])):
                x += str(lt[i][j])+" "
            print(x)
        

    def coinChange(self,n,coins):
        coinsCount = len(coins)
        dp = [[0 for x in range(n+1)] for x in range(coinsCount+1)]

        dp[0][0] = 1
        for i in range(1,n+1):
            dp[0][i] = 0
        for i in range(1,coinsCount+1):
            dp[i][0] = 1
        
        for row in range(1,coinsCount+1):
            for col in range(1,n+1):
                dp[row][col] = dp[row-1][col] + dp[row][col-coins[row-1]]
        self.printer(dp)
        return dp[coinsCount][n]

        

s = Solution()
n = 5
coins = [1,2,5]


print(s.coinChange(n,coins))

