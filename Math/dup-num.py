import math
class Solution:
    def findDuplicate(self, nums):
        for i in range(len(nums)):
            if nums[abs(nums[i])] < 0:
                return abs(nums[i])
            else:
                nums[abs(nums[i])] = -nums[abs(nums[i])]

s = Solution()
A = [3,1,3,4,2]
print(s.findDuplicate(A))