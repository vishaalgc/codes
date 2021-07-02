class Solution:
    def printer(self,lt):
        for i in range(len(lt)):
            x = ''
            for j in range(len(lt[i])):
                x += str(lt[i][j])+" "
            print(x)
        

    def lcs(self,A,B,m,n):
        if m == 0 or n == 0:
            return 0
        elif A[m-1] == B[n-1]:
            return 1 + self.lcs(A,B,m-1,n-1)
        else:
            return max(self.lcs(A,B,m,n-1), self.lcs(A,B,m-1,n))

A = "abcba"
B = "abcbcba"
s = Solution()
print(s.lcs(A,B,len(A),len(B)))