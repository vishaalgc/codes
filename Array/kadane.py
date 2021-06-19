def maxSubArray( nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    max_ending_here = 0
    max_so_far = 0
    for i in nums:
        max_ending_here += i
        if max_ending_here < 0:
            max_ending_here = 0
        max_so_far = max(max_so_far, max_ending_here)
        
    if max_so_far == 0:
        return max(nums)
    return max_so_far

A = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(A))