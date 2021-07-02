"""
Min Cost Path | DP-6
"""

class Solution:

    def printer(self,lt):
        for i in range(len(lt)):
            x = ''
            for j in range(len(lt[i])):
                x += str(lt[i][j])+" "
            print(x)

    def minCostPath(self,A):

        rows = len(A)
        cols = len(A[0])
        dp = [[0 for x in range(cols)] for x in range(rows)]

        dp[0][0] = A[0][0]
        for row in range(1,rows):
            dp[row][0] = dp[row-1][0] + A[row][0]
        
        for col in range(1,cols):
            dp[0][col] = dp[col-1][0] + A[0][col]
        
        for row in range(1,rows):
            for col in range(1,cols):
                dp[row][col] = A[row][col] + max( dp[row-1][col-1] , dp[row-1][col], dp[row][col-1] )
    
        
        self.printer(dp)
        return dp[rows-1][cols-1]


s = Solution()
A = [[1,2,3],[4,8,2],[1,5,3]]
A = [[348,391],[618,193]]

print(s.minCostPath(A))

