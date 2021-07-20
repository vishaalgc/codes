
"""
https://leetcode.com/problems/find-all-anagrams-in-a-string/
"""
class Solution:
    def findAnagrams(self, s: str, p: str):
        sLen = len(s)
        pLen = len(p)
        
        if pLen > sLen:
            return []
            
        pMap = [0]*26
        for i in p:
            elem = ord(i)-ord('a')
            pMap[elem] += 1
        
        sMap = [0]*26
        end = 0
        while end < pLen-1:
            elem = ord(s[end])-ord('a')
            sMap[elem] += 1
            end += 1
        
        start = 0
        ans = []
        while end < sLen:
            elem = ord(s[end])-ord('a')
            sMap[elem] += 1
            end+=1
            
            if sMap == pMap:
                ans.append(start)
                
            startElem = ord(s[start])-ord('a')
            sMap[startElem]-=1
            start+=1
        
        return ans
            
            
            
            
                
                
        
        
            
s = "cbaebabacd"
p = "abc"
S = Solution()
print(S.findAnagrams(s,p))            
                
                
        
        