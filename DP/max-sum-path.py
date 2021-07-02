"""
Maximum path sum in matrix
https://practice.geeksforgeeks.org/problems/path-in-matrix3805/1#
"""

class Solution:

    def printer(self,lt):
        for i in range(len(lt)):
            x = ''
            for j in range(len(lt[i])):
                x += str(lt[i][j])+" "
            print(x)
        

    def minCostPath(self,A):
        n = len(A)
        dp = [[0 for x in range(n)] for x in range(n)]

        for i in range(n):
            dp[0][i] = A[0][i]
        
        for row in range(1,n):
            for col in range(0,n):
                dp[row][col] = A[row][col] + max( dp[row-1][col], dp[row-1][col+1] if col+1 < n else -1, (dp[row-1][col-1] if col-1 >= 0 else -1)  )

        self.printer(dp)
        maxVal = -1
        for col in range(n):
            maxVal = max(maxVal,dp[n-1][col])
        return maxVal

s = Solution()
A = [[1,2,3],[4,8,2],[1,5,3]]
A = [[348,391],[618,193]]

print(s.minCostPath(A))

