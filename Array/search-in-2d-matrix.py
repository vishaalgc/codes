class Solution:
    
    def findInRow(self,row,col,cc,target,matrix):
        for i in range(col,cc):
            if matrix[row][i] == target:
                return True,(row,i)
            elif matrix[row][i] > target:
                return False,(row,i-1)
        return False,None
    
    def findInCol(self,row,col,rc,target,matrix):
        for i in range(row,rc):
            if matrix[i][col] == target:
                return True,(i,col)
            elif matrix[i][col] > target:
                return False,(i-1,col)
        return False,None
    
    def searchMatrix(self, matrix, target: int) -> bool:
        
        rc = len(matrix)
        cc = len(matrix[0])
        
        row = 0
        col = 0
        
        while row < rc or col < cc:
            print(row,col)
            found1 = False
            found2 = False
            item1 = None
            item2 = None
            if row < rc:
                found1,item1 = self.findInRow(row,col,cc,target,matrix)
            if col < cc:
                found2,item2 = self.findInCol(row,col,rc,target,matrix)
            print(item1,found1,item2,found2)
            if found1 or found2:
                return True
            if item1 == None and item2 == None:
                row+=1
                col+=1
                continue
                
            if item1 != None:
                # check in that col
                f,ans = self.findInCol(item1[0],item1[1],rc,target,matrix)
            else:
                f,ans = self.findInRow(item2[0],item2[1],cc,target,matrix)
                # print(f,ans)
            
            return f

matrix = [[1,3,5,7,9],[2,4,6,8,10],[11,13,15,17,19],[12,14,16,18,20],[21,22,23,24,25]]
target = 13
                
s = Solution()
print(s.searchMatrix(matrix,target))
                
            
                
        
        
            
        