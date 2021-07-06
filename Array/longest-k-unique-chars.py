class Solution:
    
    def isValid(self,count,k):
        sm = 0
        for i in count:
            if i > 0:
                sm += 1
        if sm > k:
            return False
        return True

    def getLongSubStr(self,s,k):
        start,end = 0,0
        n = len(s)
        res = 0
        count = [0]*26
        start = 0
        maxVal = 0
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            while start < i and not self.isValid(count,k):
                count[ord(s[start]) - ord('a')]-=1
                start+=1
            maxVal = max(maxVal,i-start+1)
        return maxVal

    def checkPossibility(self,s,k):
        mp = {}
        for i in s:
            mp[i] = True
        if len(mp.keys()) < k:
            return False
        return True
            
            
            
    
    def longestKSubstr(self, s, k):
        # code here(
        if self.checkPossibility(s,k):
            return self.getLongSubStr(s,k)
        return -1

s = Solution()
M = "aaaa"
K = 2
print(s.longestKSubstr(M,K))