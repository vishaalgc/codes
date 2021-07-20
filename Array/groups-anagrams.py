class Solution:
    
    def areGrams(self,str1,str2):
        mp = {}
        for i in str1:
            if i in mp:
                mp[i]+=1
            else:
                mp[i]=1
        for i in str2:
            if i not in mp:
                return False
            mp[i]-=1
            if mp[i]==0:
                del mp[i]
        
        
        val = len(mp.keys()) == 0
        return val
                
    
    def groupAnagrams(self, strs):
        visited = {}
        out = []
        for i in range(len(strs)):
            if i not in visited:
                cur = [strs[i]]
                for j in range(i+1,len(strs)):
                    if j not in visited:
                        if self.areGrams(strs[i],strs[j]):
                            cur.append(strs[j])
                            visited[j] = True
                visited[i] = True
                out.append(cur)
        return out

s = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
print(s.groupAnagrams(strs))