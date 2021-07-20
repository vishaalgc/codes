class Solution:
    found = False
    visited = {}
    def getStartingPoints(self,board,char,rc,cc):
        out = []
        for row in range(rc):
            for col in range(cc):
                if board[row][col] == char:
                    out.append((row,col))
        return out
    
    def getValidAdj(self,board,char,item,rc,cc):
        out = []
        row,col = item
        if 0 <= row-1 < rc and board[row-1][col] == char and (row-1,col) not in self.visited:
            out.append((row-1,col))
        if 0 <= row+1 < rc and board[row+1][col] == char and (row+1,col) not in self.visited:
            out.append((row+1,col))
        if 0 <= col-1 < cc and board[row][col-1] == char and (row,col-1) not in self.visited:
            out.append((row,col-1))
        if 0 <= col+1 < cc and board[row][col+1] == char and (row,col+1) not in self.visited:
            out.append((row,col+1))
        return out        
        
                               
    def exist(self, board, word: str) -> bool:
        rc = len(board)
        cc = len(board[0])
        starters = self.getStartingPoints(board,word[0],rc,cc)
        if not starters:
            return False
        
        def recur(items,wordIndex):
            if items and wordIndex == len(word):
                self.found = True
                return
            if wordIndex < len(word):
                for item in items:
                    self.visited[item] = True
                    adj = self.getValidAdj(board,word[wordIndex],item,rc,cc)
                    recur(adj,wordIndex+1)
                    del self.visited[item]
        recur(starters,1)
        return self.found
                
            
            
s = Solution()
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCB"
print(s.exist(board,word))

        
                               
                               
        
        
    