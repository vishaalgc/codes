
import heapq
class Element:

    def __init__(self,val,freq):
        self.val = val
        self.freq = freq
    
    def __lt__(self, other):
        return self.freq > other.freq


class Solution(object):
    def rearrangeBarcodes(self, barcodes):
        """
        :type barcodes: List[int]
        :rtype: List[int]
        """
        heap = []
        mp = {}
        for i in barcodes:
            if i in mp:
                mp[i]+=1
            else:
                mp[i]=1
        
        for key in mp.keys():
            e = Element(key,mp[key])
            heapq.heappush(heap, e)
        
        out = []

        while True:
            if not heap:
                break
            e1 = heapq.heappop(heap)
            e2 = None
            if len(heap) > 0:
                e2 = heapq.heappop(heap)
            out.append(e1.val)
            if e1.freq > 1:
                e1.freq-=1
                heapq.heappush(heap,e1)
            
            if e2:
                out.append(e2.val)
                if e2.freq > 1:
                    e2.freq-=1
                    heapq.heappush(heap,e2)
            
        return out
            


s = Solution()
codes = [1,1,1,1,2,2,3,3]

print(s.rearrangeBarcodes(codes))
