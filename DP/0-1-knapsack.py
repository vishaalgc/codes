class Solution:
    
    def printer(self,lt):
        for i in range(len(lt)):
            x = ''
            for j in range(len(lt[i])):
                x += str(lt[i][j])+" "
            print(x)

    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
        # code here
        rowsCount = len(wt)
        colsCount = W
        
        dp = [[0 for x in range(colsCount+1)] for x in range(rowsCount+1)]
        
        for row in range(1,rowsCount+1):
            for col in range(0,colsCount+1):
                weight = wt[row-1]
                if weight > col:
                    dp[row][col] = dp[row-1][col]
                    continue
                if col-wt[row-1] < 0:
                    v = 0
                else:
                    # here below we are doing row-1 because we have only one quantity of per weight
                    v = dp[row-1][col-wt[row-1]]
                dp[row][col] = max(dp[row-1][col],v+val[row-1])
                
        
        self.printer(dp)
        return dp[rowsCount][colsCount]


N = 4
W = 5
vals = [30,50,70, 60]
wts = [2, 3, 4, 5]

N = 3
W = 4
vals = [1,2,3]
wts = [4,5,1]



s = Solution()
print(s.knapSack(W,wts,vals,N))