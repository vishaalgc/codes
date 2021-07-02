"""
https://leetcode.com/problems/string-matching-in-an-array/
"""


class Solution(object):
    
    
    def matchTwoStrings(self,s,pat,lps):
        i,j=0,0
        while j < len(pat) and i < len(s):
            print(i,j)
            if s[i] == pat[j]:
                i+=1
                j+=1
            else:
                if j != 0:
                    j = lps[j-1]
                else:
                    i+=1
        return True if j == len(pat) else False    
    
    def getLps(self,s):
        lps = [0]
        i = 1
        j = 0
        n = len(s)
        while i < n:
            print(i,j,s,lps)
            if s[i] == s[j]:
                j+=1
                lps.append(j)
                i+=1
            else:
                if j != 0:
                    j = lps[j-1]
                else:
                    lps.append(0)
                    i+=1
        return lps
                
    
    
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        words.sort()
        words = list(sorted(words,key = len))
        out = []
        for patIndex in range(len(words)-1):
            lps = self.getLps(words[patIndex])
            for sIndex in range(patIndex+1,len(words)):
                if self.matchTwoStrings(words[sIndex],words[patIndex],lps):
                    out.append(words[patIndex])
                    break
        
        return out
                    

s = Solution()
words = ["mass","as","hero","superhero"]
words = ["leetcode","et","code"]
words = ["leetcoder","leetcode","od","hamlet","am"]
words = ["zjc","ezjc","xtwo","zzjc","jwx","awzzjcv"]
words = ["xu","xxu","xdea","exxusn","cs","bkcs"]
# words = ["blue","green","bu"]
print(s.stringMatching(words))

                
                
                
                
        
        
        
        