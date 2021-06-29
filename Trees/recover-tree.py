# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution(object):  
    c = 0      
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        
        def swap(p1,p2):
            temp = p1.val
            p1.val = p2.val
            p2.val = temp
        
        def recur(root,mini,maxi):
            if not root:
                return
            if mini:
                if root.val < mini.val:
                    swap(root,mini)
                    self.c+=1
            if maxi:
                if root.val > maxi.val:
                    swap(root,maxi)
                    self.c+=1
            recur(root.left,mini,root)
            recur(root.right,root,maxi)
        
        
        recur(root,None,None)
        while self.c != 0:
            self.c = 0
            recur(root,None,None)

    
head = TreeNode(2)
head.left = TreeNode(3)
head.right = TreeNode(1)

s = Solution()
s.recoverTree(head)

        
        
                
            
            
        