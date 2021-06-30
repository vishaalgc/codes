class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        

        def recur(openC,closeC,lt,out,n):
            if closeC > openC:
                return
            if openC == closeC == n:
                item = ''.join(lt)
                if item not in out:
                    out.append(item)

            if openC <= n:
                lt.append('(')
                openC+=1
                recur(openC,closeC,lt,out,n)
                openC-=1
                lt.pop()
            if closeC <= n:
                lt.append(')')
                closeC+=1
                recur(openC,closeC,lt,out,n)
                closeC-=1
                lt.pop()
        
        out = []
        recur(0,0,[],out,n)
        return out

s = Solution()
print(s.generateParenthesis(3))