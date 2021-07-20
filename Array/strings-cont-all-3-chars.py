"""
https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/
"""
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        cur_dict = {}
        start = 0
        ans = 0
        for end in range(len(s)):
            cur_dict[s[end]]=cur_dict.get(s[end],0)+1
            if len(cur_dict.keys()) == 3:
                ctr = 0
                while len(cur_dict.keys()) == 3:
                    ctr += 1
                    cur_dict[s[start]]-=1
                    if cur_dict[s[start]] == 0:
                        del cur_dict[s[start]]
                    start+=1

                appender = len(s)-end
                ans += ctr * appender
                

        return ans
        
s = Solution()
st = "acbbcac"
st = "abcabc"
print(s.numberOfSubstrings(st))
