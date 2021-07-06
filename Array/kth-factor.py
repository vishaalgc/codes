import math
class Solution:
    def kthFactor(self, A: int, k: int) -> int:
        
        x = []
        i = 1
        n = int(math.sqrt(A))
        
        while i <= n:
            if A%i == 0:
                x.append(i)
                val = A//i
                if val not in x:
                    x.append(val)
            i+=1
        x.sort()
        print(x)
        if k-1 < len(x):
            return x[k-1]
        return -1
                
        
s = Solution()
print(s.kthFactor(7,2))