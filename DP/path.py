class Solution:
    """
    1 2 3
    4 5 6
    """
    def minPathSum(self, dp):
        
        rc = len(dp)
        cc = len(dp[0])
        
        
        for col in range(1,cc):
            dp[0][col] += dp[0][col-1]
        
        for row in range(1,rc):
            dp[row][0] += dp[row-1][0]
        
        for row in range(1,rc):
            for col in range(1,cc):
                dp[row][col] += min(dp[row-1][col],dp[row][col-1])
        
        print(dp)
        return dp[rc-1][cc-1]
 
s = Solution()
grid = [[1,2,3],[4,5,6]]
grid = [[1,2],[1,1]]
print(s.minPathSum(grid))
