"""
https://leetcode.com/problems/top-k-frequent-words/
"""

import heapq
class Element:
    def __init__(self,val,freq):
        self.val = val
        self.freq = freq
    
    def __lt__(self,other):
        return self.freq >= other.freq


class Solution:
    def topKFrequent(self, words, k: int):
        heap = []
        
        mp = {}
        for word in words:
            mp[word] = mp.get(word,0)+1
        
        
        out = []
        print(mp)
        for word in mp.keys():
            if mp[word] >= k:
                out.append(word)
        out.sort()
        return out
        # while heapq:
        #     elem = heapq.heappop(heap)
        #     if elem.freq == k:
        #         out.append(elem.val)
        #     if elem.freq < k:
        #         break
        
        out.sort()
        return out
        
        
    
items = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
k = 4
s = Solution()
print(s.topKFrequent(items,k))