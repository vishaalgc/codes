class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        st = 'abcdef'
        out = []
        
        if num == 0:
            return '0'
        
        if num<0:
            num = 2**32+num
        
        while num:
            num,rem = divmod(num,16)
            if rem >= 10:
                rem-=10
                rem=st[rem]
            rem = str(rem)
            out.append(rem)
        
        out = out[::-1]
        return ''.join(out)

s= Solution()
num = 26
print(s.toHex(num))