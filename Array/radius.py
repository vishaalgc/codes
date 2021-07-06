"""
https://leetcode.com/problems/heaters/
"""

class Solution:
    def findRadius(self, houses, heaters):
        
        
        
        def isBounded(heaters,left,right,h):
            if h <= heaters[left]:
                return heaters[left]
            if h >= heaters[right]:
                return heaters[right]
            return getNearest(heaters,left,right,h)
        
        def getNearest(heaters,left,right,h):
            if right < left:
                return heaters[right]
            if right-left == 1:
                if h - heaters[left] < heaters[right] - h:
                    return heaters[left]
                return heaters[right]
            mid = (left+right)//2
            if heaters[mid] == h:
                return h
            elif h > heaters[mid]:
                return getNearest(heaters,mid,right,h)
            else:
                return getNearest(heaters,left,mid,h)
            
        
        n = len(heaters)
        heaters.sort()
        rad = 0
        for h in houses:
            val = isBounded(heaters,0,n-1,h)
            rad = max(rad,abs(val-h))
        return rad
            
            
s = Solution()  
houses = [1,2,3,4]
heaters = [1,4]
print(s.findRadius(houses,heaters))
        
    
        
            
            
            