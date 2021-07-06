import heapq
class Element:
    
    def __init__(self,val):
        self.val = val
    def __lt__(self, other):
        return self.val > other.val
    
class Solution:
    def kthSmallest(self, matrix, k):
        heap = []
        maxSize = k 
        rowsCount = len(matrix)
        colsCount = len(matrix[0])
        for row in range(rowsCount):
            for col in range(colsCount):
                val = matrix[row][col]
                e = Element(val)
                if len(heap) == k:
                    if val <= heap[0].val:
                        heapq.heappop(heap)
                        heapq.heappush(heap,e)
                else:
                    heapq.heappush(heap,e)
        # if heap:
        #     return heap[0].val
        for i in heap:
            print(i.val)
                    
                    
                
        
                    
                    
matrix = [[1,4],[2,5]]
k = 2
s = Solution()
print(s.kthSmallest(matrix,k))
                
        