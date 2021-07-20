class Solution:
    
    def handlePops(self,st,runningIndex,arr):
        poppedIndex = st[-1]
        st.pop()
        if st:
            return (runningIndex-st[-1]-1)*arr[poppedIndex]
        else:
            return (runningIndex)*arr[poppedIndex]
        
    

    def maxAreaIn1D(self,arr):
        
        st = []
        maxArea = 0
        i = 0
        n = len(arr)
        while i < n:
            if not st or arr[i] >= arr[st[-1]]:
                st.append(i)
                i+=1
            else:
                area = self.handlePops(st,i,arr)
                maxArea = max(maxArea,area)
        while st:
            area = self.handlePops(st,n,arr)
            maxArea = max(maxArea,area)
        print(arr,maxArea)
        return maxArea
    
    def addARow(self,row,arr,matrix):
        col = 0
        for i in range(len(arr)):
            if matrix[row][col] == '0':
                arr[i] = 0
            else:
                arr[i] += int(matrix[row][col])
            col+=1                
            
    
    def maximalRectangle(self, matrix) -> int:
        maxArea = 0
        if not matrix:
            return 0
        rc,cc = len(matrix),len(matrix[0])
        tempArr = [0]*cc
        for row in range(rc):
            self.addARow(row,tempArr,matrix)
            area = self.maxAreaIn1D(tempArr)
            maxArea = max(maxArea,area)
        return maxArea
        
s = Solution()
matrix = [["1"]]
matrix = [["0","1"],["1","0"]]
print(s.maximalRectangle(matrix))