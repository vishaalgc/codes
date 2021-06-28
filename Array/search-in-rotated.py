class Solution(object):
    
    def bs(self,nums,i,j,b):
        
        if j < i:
            return -1
        mid = (i+j)//2
        if nums[mid] == b:
            return mid
        print(i,j,nums[mid])
        # check which part is sorted
        if nums[mid] < nums[j]:
            if nums[j] >= b > nums[mid]:
                return self.bs(nums,mid+1,j,b)
            else:
                return self.bs(nums,i,mid-1,b)
        
        else:
            if nums[mid] > b  >= nums[i]:
                return self.bs(nums,i,mid-1,b)
            else:
                return self.bs(nums,mid+1,j,b)
        
    
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        return self.bs(nums,0,len(nums)-1,target)

s = Solution()
nums = [4,5,6,7,0,1,2]
target = 0
x = s.search(nums,target)
print(x)
