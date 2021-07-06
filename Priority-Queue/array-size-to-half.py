"""
https://leetcode.com/explore/challenge/card/july-leetcoding-challenge-2021/608/week-1-july-1st-july-7th/3804/
"""

import heapq

class Element:
    def __init__(self,val,freq):
        self.val = val
        self.freq = freq
    
    def __lt__(self,other):
        return self.freq > other.freq
    
class Solution:
    def minSetSize(self, arr):
        heap = []
        mp = {}
        totalSize = len(arr)
        for item in arr:
            if item in mp:
                mp[item]+=1
            else:
                mp[item]=1
        
        for key in mp.keys():
            e = Element(key,mp[key])
            heapq.heappush(heap,e)
        
        count = 0
        targetSize = totalSize//2
        sz = totalSize
        while heap and sz > targetSize:
            elem = heapq.heappop(heap)
            count+=1
            sz -= elem.freq
        return count

s = Solution()
arr = [3,3,3,3,5,5,5,2,2,7]
arr =[7,7,7,7,7,7]
arr = [1,9]
print(s.minSetSize(arr))

                    
        