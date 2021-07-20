class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        rc = len(matrix)
        cc = len(matrix[0])
        
        dp = [[0 for x in range(cc+1)] for x in range(rc+1)]
        ans = 0
        for row in range(1,rc+1):
            for col in range(1,cc+1):
                if matrix[row-1][col-1] == '1':
                    dp[row][col] = min(dp[row-1][col],dp[row-1][col-1],dp[row][col-1])+1
                    ans = max(ans,dp[row][col])

        return ans*ans
        