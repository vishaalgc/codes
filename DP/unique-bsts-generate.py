class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        
        # dp = [[-1 for x in range(n+1)] for x in range(n+1)]
        
        def recur(start,end):
            out = []
            if start > end:
                out.append(None)
                return out
            # if dp[start][end] != -1:
            #     return dp[start][end]
            
            for i in range(start,end+1):
                left = recur(start,i-1)
                right = recur(i+1,end) 
                for l in left:
                    for r in right:
                        node = TreeNode(i)
                        node.left = l
                        node.right = r
                        out.append(node)
            
            # dp[start][end] = list(out)
        return recur(1,n)

s = Solution()
p = s.generateTrees(5)
print(len(p))