import sys
class Solution():
    
    def getSum(self,stones,i,j):
        return sum(stones[i:j+1])
    
    
    def getBestSlidingWindow(self,stones,k):
        bestWindow = (0,k-1)
        bestSum = self.getSum(stones,0,k-1)
        for i in range(len(stones)-(k-1)):
            j = i+k-1
            sm = self.getSum(stones,i,j)
            if sm < bestSum:
                bestWindow = (i,j)
                bestSum = sm
        return bestWindow,bestSum
    
    def merger(self,stones,i,j,sm):
        out = []
        set = False
        for k in range(len(stones)):
            if k < i or k > j:
                out.append(stones[k])
            else:
                if not set:
                    out.append(sm)
                    set = True
        return out
            
        
        
    def mergeStones(self, stones, k, cost):
        """
        :type stones: List[int]
        :type k: int
        :rtype: int
        """
        if len(stones) == k:
            return sum(cost)+sum(stones)
        if len(stones) < k:
            return -1
        
        
        (i,j),bestSum = self.getBestSlidingWindow(stones,k)
        stones = self.merger(stones,i,j,bestSum)
        cost.append(bestSum)
        print((i,j),bestSum )
        return self.mergeStones(stones,k,cost)
        
    
        
s = Solution()
stones =  [6,4,4,6]
k = 2
print(s.mergeStones(stones,k,[]))

        
        
        