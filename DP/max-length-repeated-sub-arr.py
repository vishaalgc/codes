"""
https://leetcode.com/problems/maximum-length-of-repeated-subarray/
"""

class Solution(object):
    def maxLength(self, arr1,arr2):

        rowsCount = len(arr1)
        colsCount = len(arr2)

        dp = [[0 for x in range(colsCount+1)] for x in range(rowsCount+1)]

        for row in range(rowsCount+1):
            dp[row][0] = 0
        
        for col in range(colsCount+1):
            dp[0][col] = 0

        maxVal = -1
        for row in range(1,rowsCount+1):
            for col in range(1,colsCount+1):
                if arr1[row-1] == arr2[col-1]:
                    dp[row][col] = dp[row-1][col-1]+1
                    maxVal = max(maxVal,dp[row][col])

        return maxVal

        # A = [3,7,8,9,15]
        # x = []
        # for i in range(1,len(A)):
        #     x.append(A[i] & A[i-1])

        # print(x)


        
                
        
        

s = Solution()
nums1 = [1,2,3,2,1]
nums2 = [3,2,1,4,7]

nums1 = [0,0,0,0,0]
nums2 = [0,0,0,0,0]
print(s.maxLength(nums1,nums2))