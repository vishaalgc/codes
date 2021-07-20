class Solution:
    def canJump(self) -> bool:
        farthest = 0
        for i in range(len(nums)):
            if farthest < i:
                return False
            farthest = max(i+nums[i],farthest)
        
        return True
            
s = Solution()
nums = [2,3,1,1,4]
nums = [3,2,1,0,4]
print(s.canJump(nums))