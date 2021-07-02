class Solution(object):
    
    def bs(self,i,j,num):
        if j < i:
            return False
        val = (i+j)//2
        elem = val*val
        if elem == num:
            return True
        if elem < num:
            return self.bs(val+1,j,num)
        return self.bs(i,val-1,num)
        
    
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return self.bs(0,num,num)

c = Solution()
A = 0
print(c.isPerfectSquare(A))