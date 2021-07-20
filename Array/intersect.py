class Solution:
    
    def intersect(self, nums1, nums2):
        if len(nums1) < len(nums2):
            nums1,nums2 = nums2,nums1
            
        # nums1 is always bigger
        # lets try sorting
        nums1.sort()
        nums2.sort()
        
        out = []
        start = 0
        i = 0
        print(nums1)
        print(nums2)
        while start < len(nums2) and i < len(nums1):
            if nums1[i] == nums2[start]:
                out.append(nums1[i])
                start+=1
                i+=1
            elif nums1[i] < nums2[start]:
                i+=1
            else:
                start+=1

        return out

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
s = Solution()
print(s.intersect(nums1,nums2))
                
            
        