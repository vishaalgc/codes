class Solution:
    
    """
    1. have start, end pointers. 
    2. Recur function. Find an item between start and end which is repeating < k
    3. keep it as mid.
    4. Recur Max for < mid and > mid
    https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/
    """
    
    def longestSubstring(self, s: str, k: int) -> int:
        
        def getMap(s):
            mp = {}
            for i in s:
                if i in mp:
                    mp[i]+=1
                else: 
                    mp[i]=1
            return mp
                    
                
        mp = getMap(s)
        def recur(start,end,s,k):
            print(start,end)
            if end < start:
                return 0
            for i in range(start,end+1):
                if mp[s[i]] < k:
                    mid = i
                    return max(recur(start,mid-1,s,k),recur(mid+1,end,s,k))
            return end-start
        
        return recur(0,len(s)-1,s,k)+1

s = Solution()
st = "ababacb"
k = 3
print(s.longestSubstring(st,k))
        
        
        
            
        