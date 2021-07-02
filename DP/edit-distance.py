"""
Edit Distance | DP-5
"""

class Solution():


    def printer(self,lt):
        for i in range(len(lt)):
            x = ''
            for j in range(len(lt[i])):
                x += str(lt[i][j])+" "
            print(x)

    def editDistanceDp(self,s1,s2):

        m = len(s1)
        n = len(s2)
        dp = [[0 for x in range(n+1)] for x in range(m+1)]

        for row in range(0,m+1):
            for col in range(0,n+1):
                if row == 0:
                    dp[row][col] = col
                elif col == 0:
                    dp[row][col] = row
                elif s1[row-1] == s2[col-1]:
                    dp[row][col] = dp[row-1][col-1]
                else:
                    dp[row][col] = 1 + min( dp[row-1][col-1], dp[row-1][col], dp[row][col-1])
        # self.printer(dp)
        return dp[m][n]


    def editDistance(self,s1,s2):
        def recur(s1,s2,m,n,memo):
            if m == 0:
                return n
            if n == 0:
                return m
            
            if s1[m-1] == s2[n-1]:
                return recur(s1,s2,m-1,n-1,memo)
            
            if (m,n) in memo:
                return memo[(m,n)]

            ins = recur(s1,s2,m,n-1,memo)
            rem = recur(s1,s2,m-1,n,memo)
            rep = recur(s1,s2,m-1,n-1,memo)

            memo[(m,n-1)] = ins
            memo[(m-1,n)] = rem
            memo[(m-1,n-1)] = rep
            memo[(m,n)] = 1 + min(ins,rem,rep)
            return memo[(m,n)]
    
        memo = {}
        val  = recur(s1,s2,len(s1),len(s2),memo)
        # print(memo)
        return val

s = Solution()
s1 = 'dbb'
s2 = 'fdfaccddfac'
v = s.editDistanceDp(s1,s2)
print(v)