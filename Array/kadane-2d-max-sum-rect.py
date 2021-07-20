import bisect
class Solution:
    
    maxSum = -2**31
    def generateMaxSum(self,kadArr,k):
        sm = 0
        prefixSums = [0]
        maxVal = -2**31
        for i in kadArr:
            bisect.insort(prefixSums, sm)
            sm += i
            x = bisect.bisect_left(prefixSums,sm-k)
            if x != len(prefixSums):
                maxVal = max(maxVal,sm - prefixSums[x])
        
        self.maxSum = max(self.maxSum,maxVal)
        
        
    def addToKadArr(self,kadArr,matrix,rowsCount,col):
        r = 0
        for i in range(len(kadArr)):
            kadArr[i] += matrix[r][col]
            r+=1
    
    
    def maxSumSubmatrix(self, matrix, k):
        rowsCount = len(matrix)
        colsCount = len(matrix[0])        
        for l in range(colsCount):
            kadArr = [0]*rowsCount
            for r in range(l,colsCount):
                print("l,r",l,r)
                self.addToKadArr(kadArr,matrix,rowsCount,r)
                self.generateMaxSum(kadArr,k)
        
        return self.maxSum
                
                

s = Solution()
M = [[5,-4,-3,4],[-3,-4,4,5],[5,1,5,-4]]
k = 8
print(s.maxSumSubmatrix(M,k))
                

# 5 -4 -3  4
# -3 -4  4  5
# 5  1  5 -4
                