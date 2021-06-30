class Solution(object):
    def printer(self,dp,n):
        for row in range(n):
            out = ''
            for col in range(n):
                out+=str(dp[row][col])+' '
            print(out)

    def getBoolDp(self,s,n):
        dp = [[False for x in range(n)] for x in range(n)]
        for i in range(n):
            dp[i][i] = True

        row = 0
        col = 1
        rows_count,cols_count = n,n
        while True:
            lastCol = col
            if lastCol == cols_count:
                break
            while row < rows_count and col < cols_count:
                if s[row] == s[col] and (col-row <= 1 or dp[row+1][col-1] == True):
                    dp[row][col] = True
                row+=1
                col+=1
            row = 0
            col = lastCol+1
        return dp
    
    def checkForParts(self,startIndex,partitions,dp,n):
        if partitions == 1:
            if startIndex == n:
                return False
            return dp[startIndex][n-1]
        
        for col in range(startIndex,n):
            if dp[startIndex][col] and self.checkForParts(col+1,partitions-1,dp,n):
                return True
        return False
                
            
    
    
    def checkPartitioning(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        dp = self.getBoolDp(s,n)
        # self.printer(dp,n)
        return self.checkForParts(0,3,dp,n)

x = Solution()
s = "juchzcedhfesefhdeczhcujzzvbmoeombv"
print(x.checkPartitioning(s))

