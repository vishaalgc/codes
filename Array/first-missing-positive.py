class Solution:

    def swap(self,i,j,nums):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp

    
    def firstMissingPositive(self, nums):
        for i in range(len(nums)):
            while nums[i] > 0 and nums[i] <= len(nums) and nums[nums[i]-1] != nums[i]:
                self.swap(i,nums[i]-1,nums)
                  
        for i in range(len(nums)):
            if nums[i] != i+1:
                return i+1
        return len(nums)+1
            
        
        
s = Solution()
# nums = [1,2,0]
# nums = [3,4,-1,1]
nums = [1,8,9,11,12]
nums = [1]
nums = [-1,-2,-60,40,43]
nums = [-1,4,2,1,9,10]
print(s.firstMissingPositive(nums))
