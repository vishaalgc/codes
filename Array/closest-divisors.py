import math
class Solution:
    
    def closestDivisors(self, num: int):
        for i in range(int(math.sqrt(num+2)),0,-1):
            print(i,num+1)
            if (num+1) % i == 0:
                return [i,(num+1)//i]
            elif (num+2)% i == 0:
                return [i,(num+2)//i]
    
        return []
        

num = 2
s = Solution()
print(s.closestDivisors(num))
