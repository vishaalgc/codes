"""
https://leetcode.com/problems/guess-number-higher-or-lower/
"""


def guess(num):
    if num == 6:
        return 0
    if num > 6:
        return 1
    return -1
class Solution:
    def guessNumber(self, n: int) -> int:
        
        def bs(start,end):
            mid = (start + end)//2
            val = guess(mid)
            if val == 0:
                return mid
            elif val == -1:
                return bs(start,mid-1)
            return bs(mid+1,end)
        return bs(1,n)

n = 10
s = Solution()
print(s.guessNumber(n))
        