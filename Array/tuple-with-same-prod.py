"""
https://leetcode.com/problems/tuple-with-same-product/
"""

class Solution:
    
    def fact(self,n):
        if n == 0:
            return 1
        val = 1
        while n != 1:
            val*=n
            n-=1
        return val
    
    def ncr(self,n,r):
        return (n*(n-1))//2
        # return self.fact(n) // (self.fact(r) * self.fact(n-r))
    
    def tupleSameProduct(self, nums):
        mp = {}
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                val = nums[i]*nums[j]
                if val in mp:
                    mp[val]+=1
                else:
                    mp[val]=1
        ans = 0
        for key in mp.keys():
            val = mp[key]
            if val >= 2:
                ans += self.ncr(val,2) * 8
        
        return ans
                

s = Solution()
nums = [2,3,4,6]
nums = [1,2,4,5,10]
nums = [2,3,4,6,8,12]
nums = [2,3,5,7]
print(s.tupleSameProduct(nums))

            
        