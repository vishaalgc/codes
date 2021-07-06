"""
https://leetcode.com/problems/path-with-minimum-effort/
"""
import heapq
class Solution:
    def minimumEffortPath(self, heights):
        
        rows = len(heights)
        cols = len(heights[0])
        
        def getNextNodes(row,col):
            dirs = ((0,1),(1,0),(0,-1),(-1,0))

            for d in dirs:
                nc = col + d[1]
                nr = row + d[0]
                if 0 <= nr < rows and 0 <= nc < cols:
                    yield (nr,nc)
                    
        
        visited = {}
        heap = []
        heapq.heappush(heap,(0,(0,0)))
        
        while heap:
            effort , node = heapq.heappop(heap)
            if node in visited:
                continue
            visited[node] = effort
            
            for neigh in getNextNodes(node[0],node[1]):
                print(neigh)
                ne = max(effort, abs(heights[neigh[0]][neigh[1]] - heights[node[0]][node[1]]))
                heapq.heappush(heap,(ne,neigh))
        
        return visited[(rows-1,cols-1)]
                
        



s = Solution()
heights = [[1,2,2],[3,8,2],[5,3,5]]
print(s.minimumEffortPath(heights))